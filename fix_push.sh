#!/bin/bash
git reset --soft HEAD~1 2>/dev/null || true
rm -rf .git/refs/original/
git rm -r --cached .buildozer/ bin/ __pycache__/ 2>/dev/null || true
echo ".buildozer/" > .gitignore
echo "bin/" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .
git commit -m "Clean Optimus Jarvis Push"
git push -u origin main --force
