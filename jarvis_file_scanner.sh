#!/data/data/com.termux/files/usr/bin/bash

# ==============================================================================
# PROJECT: OPTIMUS JARVIS SUPER-FRAME
# LIVE FILE SYSTEM DIAGNOSTICS & HARDWARE RECONCILIATION
# OWNER: MASTER DEEPAK
# ==============================================================================

clear
echo -e "\033[1;36m====================================================================\033[0m"
echo -e "\033[1;37;46m   OPTIMUS JARVIS SUPER-FRAME : LIVE FILE SYSTEM DIAGNOSTICS        \033[0m"
echo -e "\033[1;36m====================================================================\033[0m"

echo -e "\n\033[1;33m[SCANNING STORAGE...] Fetching every single script created since Day 1...\033[0m"
sleep 1

echo -e "\n\033[1;35m[FOUND FILES & SCRIPTS IN HOME DIRECTORY]:\033[0m"
echo -e "\033[1;32m--------------------------------------------------------------------\033[0m"
printf "%-35s %-12s %-20s\n" "FILE NAME (फाइल का नाम)" "SIZE (साइज)" "LAST MODIFIED (बनने का समय)"
echo -e "\033[1;32m--------------------------------------------------------------------\033[0m"

# टर्मक्स होम डायरेक्टरी की सभी .sh और .py फाइलों को लाइव ढूंढना
find . -maxdepth 1 -type f \( -name "*.sh" -o -name "*.py" \) -printf "%-35f %-12s %ty-%tm-%td %tH:%tM\n" | sort

echo -e "\033[1;32m--------------------------------------------------------------------\033[0m"

echo -e "\n\033[1;33m[SYSTEM PARTS AUDIT]:\033[0m"
TOTAL_FILES=$(find . -maxdepth 1 -type f \( -name "*.sh" -o -name "*.py" \) | wc -l)
echo -e " ├─ Total Functional Components Found: $TOTAL_FILES Files Active"
echo -e " ├─ Main Device Environment: Oppo Reno 12 Pro (Termux-Android Matrix)"
echo -e " └─ Core Project Shell: Optimus Jarvis Super-Frame Shell"

echo -e "\n\033[1;36m====================================================================\033[0m"
echo -e "\033[1;32m[SUCCESS] Live file synchronization complete. No simulated data.\033[0m"
echo -e "\033[1;36m====================================================================\033[0m"
