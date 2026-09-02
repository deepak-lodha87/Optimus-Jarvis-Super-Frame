#!/data/data/com.termux/files/usr/bin/bash

# Phase 317: Optimus Jarvis Cloud Synchronization
echo "[+] Starting Cloud Synchronization..."

# Initializing Git if not already done
if [ ! -d ".git" ]; then
    git init
    echo "[!] Git Repository Initialized."
fi

# Adding all files (alien_eng.py, fabricator.py, main_jarvis.py, etc.)
git add .

# Creating a save point with Phase Number
timestamp=$(date +"%Y-%m-%d %H:%M")
git commit -m "Backup: Phase 317 - $timestamp"

echo "[✓] Files are staged and committed locally."
echo "[INFO] Use 'git push' to send them to GitHub."
