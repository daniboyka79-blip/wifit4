#!/data/data/com.termux/files/usr/bin/env python
import os
import sys
import time
import json
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

REPO_DIR = os.path.expanduser("~/wifit4")

BANNER = f"""{BOLD}
  █   █ ▀ █▀▀ ▀ ▀█▀ █ █
  █ █ █ █ █▀  █  █  ▀▀█
  ▀▄▀▄▀ ▀ ▀   ▀  ▀    ▀
{RESET}{CYAN}    wifit4 v1.0 - GitHub + Termux{RESET}
"""

def clear():
    os.system("clear")

def scan_networks():
    print(f"\n{YELLOW}[*] Scanning Wi-Fi networks via Termux API...{RESET}")
    try:
        output = subprocess.check_output(["termux-wifi-scaninfo"], stderr=subprocess.DEVNULL)
        networks = json.loads(output.decode("utf-8"))
        if not networks:
            print(f"{RED}[!] ምንም ኔትወርክ አልተገኘም። የስልክህን Location (GPS) አብርተህ እንደገና ሞክር።{RESET}")
            return
        print(f"\n{BOLD}{'SSID':<22} {'BSSID':<19} {'SIGNAL':<10} {'FREQ'}{RESET}")
        print("-" * 62)
        for net in networks:
            ssid = net.get("ssid") or "<Hidden>"
            bssid = net.get("bssid", "N/A")
            rssi = f"{net.get('rssi', 'N/A')} dBm"
            freq = f"{net.get('frequency', 'N/A')} MHz"
            print(f"{ssid:<22} {bssid:<19} {rssi:<10} {freq}")
    except FileNotFoundError:
        print(f"{RED}[!] termux-api አልተጫነም። መጀመሪያ 'pkg install termux-api' አስገባ።{RESET}")
    except Exception as e:
        print(f"{RED}[!] ስህተት ተፈጥሯል: {e}{RESET}")

def update_from_github():
    print(f"\n{YELLOW}[*] ከ GitHub አዲስ ማሻሻያ በመፈለግ ላይ...{RESET}")
    if not os.path.exists(REPO_DIR):
        print(f"{RED}[!] የ ~/wifit4 ፎልደር አልተገኘም።{RESET}")
        return
    try:
        res = subprocess.check_output(["git", "-C", REPO_DIR, "pull"], stderr=subprocess.STDOUT)
        msg = res.decode("utf-8").strip()
        print(f"{GREEN}[+] {msg}{RESET}")
        if "Already up to date" not in msg:
            print(f"{CYAN}[*] ፕሮግራሙ በአዲሱ ኮድ እንደገና እየተከፈተ ነው...{RESET}")
            time.sleep(1.2)
            os.execv(sys.executable, [sys.executable] + sys.argv)
    except Exception as e:
        print(f"{RED}[!] Update ማድረግ አልተቻለም: {e}{RESET}")

def main():
    clear()
    print(BANNER)
    print(f"{YELLOW}   Scanning for compatible hardware...{RESET}")
    time.sleep(1.2)
    print(f"   {GREEN}[ Start ]{RESET}   {RED}[ Quit ]{RESET}\n")

    while True:
        choice = input(f"{CYAN}[s] Start  [u] Update (GitHub)  [p] Prefs  [q] Quit > {RESET}").strip().lower()
        if choice == "s":
            scan_networks()
        elif choice == "u":
            update_from_github()
        elif choice == "p":
            print(f"{YELLOW}[*] Mode: Unrooted Android | Synced with GitHub ({REPO_DIR}){RESET}")
        elif choice == "q":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
