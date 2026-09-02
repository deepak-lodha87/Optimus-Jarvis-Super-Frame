#!/data/data/com.termux/files/usr/bin/bash

echo "[+] Organizing Optimus Jarvis Super-Frame..."
mkdir -p Jarvis_Project

# Moving all files to the project folder
mv alien_eng.py fabricator.py core_bridge.py main_jarvis.py strategy.py sync_jarvis.sh Jarvis_Project/

echo "[✓] All modules moved to 'Jarvis_Project' folder."
echo "[!] To run Jarvis, type: cd Jarvis_Project && python main_jarvis.py"
