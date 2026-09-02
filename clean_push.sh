#!/bin/bash
rm -rf .git
git init
git config http.postBuffer 524288000
echo ".buildozer/" > .gitignore
echo "bin/" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .
git commit -m "Initial Clean Push for Optimus Jarvis Super Frame"
git branch -M main
git remote add origin https://github.com/deepak-lodha87/Optimus-Jarvis-Super-Frame.git
git push -u origin main --force
