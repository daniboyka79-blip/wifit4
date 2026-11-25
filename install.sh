#!/data/data/com.termux/files/usr/bin/bash
apt update -y
apt install python git termux-api -y
chmod +x ~/wifit4/wifit4.py
ln -sf ~/wifit4/wifit4.py $PREFIX/bin/wifit4
echo "[+] ተጭኗል! አሁን 'wifit4' ብለህ ስትጽፍ ይከፍታል።"
