#!/bin/bash

# Configuration
REPO_NAME="Optimus-Neural-Framework"
BRANCH="main"

# Professional Voice Feedback
optimus_speak() {
    python3 -c "import subprocess; subprocess.run(['termux-tts-speak', '$1'])"
}

clear
echo -e "\033[1;36m" + "☁️" * 30
echo -e "      OPTIMUS NEURAL SYSTEMS : AUTONOMOUS CLOUD SYNC (P356)"
echo -e "☁️" * 30 + "\033[0m"

optimus_speak "Initiating autonomous cloud synchronization protocol."

# Checking for Remote Updates
echo -e "\033[1;33m[SCANNING]: Checking for remote updates on GitHub...\033[0m"
git fetch origin $BRANCH &> /dev/null

UPSTREAM=${1:-'@{u}'}
LOCAL=$(git rev-parse @)
REMOTE=$(git rev-parse "$UPSTREAM")

if [ $LOCAL = $REMOTE ]; then
    echo -e "\033[1;32m[STATUS]: Local system is up-to-date with Cloud Archive.\033[0m"
    optimus_speak "All neural files are synchronized."
elif [ $LOCAL = $(git merge-base @ "$UPSTREAM") ]; then
    echo -e "\033[1;31m[ALERT]: New Cloud Update Detected!\033[0m"
    optimus_speak "New data detected on the cloud. Pulling updates now."
    git pull origin $BRANCH
else
    echo -e "\033[1;33m[PUSH]: Local changes detected. Synchronizing to Cloud...\033[0m"
    git add .
    git commit -m "Auto-Sync: Optimus Neural Core Update $(date +'%Y-%m-%d')"
    git push origin $BRANCH
    optimus_speak "Local data has been successfully archived to the cloud."
fi

echo -e "\033[1;36m[RESULT]: CLOUD SYNC PROTOCOL COMPLETE.\033[0m"
