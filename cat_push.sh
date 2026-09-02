#!/bin/bash
git checkout --orphan temp_branch
git rm -rf --cached .buildozer bin __pycache__ 2>/dev/null || true
echo ".buildozer/" > .gitignore
echo "bin/" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .
git commit -m "Deploy Optimus Jarvis Super Frame Core"
git branch -D main 2>/dev/null || true
git branch -m main
git push -u origin main --force
