#!/bin/bash

# Optimus Jarvis Super-Frame: Cloud Push Script
echo "Checking repository status..."

# Git commands to automate the process
git add .
read -p "Enter update message (e.g., Phase 1829 complete): " message
git commit -m "$message"

echo "Syncing with GitHub Cloud..."
git push origin main

echo "Update successful. Your progress is now permanently saved online."
