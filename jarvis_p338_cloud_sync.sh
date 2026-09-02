#!/bin/bash

# Configuration
REPO_URL="https://github.com/YOUR_USERNAME/Optimus-Jarvis-Super-Frame.git"
COMMIT_MSG="Auto-sync Jarvis Core: Phase 338 - $(date +'%Y-%m-%d %H:%M:%S')"

# Voice Feedback via Python
jarvis_speak() {
    python3 -c "import subprocess; subprocess.run(['termux-tts-speak', '$1'])"
}

echo -e "\033[1;36m====================================================="
echo -e "      JARVIS CLOUD SYNC PROTOCOL : PHASE 338"
echo -e "=====================================================\033[0m"

jarvis_speak "Initiating secure cloud synchronization to GitHub."

# Git Initialization (Only if not already a git repo)
if [ ! -d ".git" ]; then
    git init
    git remote add origin $REPO_URL
fi

# Sync Process
echo -e "\033[1;33m[STEP 1]: Staging all Jarvis Phase files...\033[0m"
git add .

echo -e "\033[1;33m[STEP 2]: Creating encrypted commit...\033[0m"
git commit -m "$COMMIT_MSG"

echo -e "\033[1;33m[STEP 3]: Pushing data to Stark Cloud (GitHub)...\033[0m"
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "\033[1;32m[SUCCESS]: Backup complete. Files are safe on Cloud.\033[0m"
    jarvis_speak "Cloud synchronization successful. Your project is now permanent."
else
    echo -e "\033[1;31m[ERROR]: Sync failed. Check internet or Git credentials.\033[0m"
    jarvis_speak "Cloud sync failed. Please check your network connection."
fi
