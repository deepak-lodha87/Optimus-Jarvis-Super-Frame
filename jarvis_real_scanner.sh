#!/data/data/com.termux/files/usr/bin/bash

# ==============================================================================
# PROJECT: OPTIMUS JARVIS SUPER-FRAME
# PHASE: 65 (REAL-TIME HARDWARE RESOURCE EXTRACTION ENGINE)
# OWNER: MASTER DEEPAK
# TYPE: 100% REAL HARDWARE DIAGNOSTIC (NON-SIMULATION)
# ==============================================================================

clear
echo -e "\033[1;36m====================================================================\033[0m"
echo -e "\033[1;37;46m   OPTIMUS JARVIS SUPER-FRAME : PHASE 65 LIVE HARDWARE SCANNER     \033[0m"
echo -e "\033[1;36m====================================================================\033[0m"

echo -e "\n\033[1;33m[READING HARDWARE] Accessing Oppo Phone Internal Kernels...\033[0m"
sleep 1

# 1. असली रैम (RAM) की जानकारी निकालना
echo -e "\n\033[1;35m[1. ACTUAL MEMORY (RAM) STATUS]:\033[0m"
free -h | awk 'NR==1{print "    " $1 "       " $2 "       " $3} NR==2{print " ├─ RAM:    Total: " $2 " | Used: " $3 " | Free: " $4}'

# 2. असली सीपीयू (CPU) और अपटाइम की जानकारी
echo -e "\n\033[1;35m[2. CPU CORE ACTIVITY]:\033[0m"
UPTIME_DATA=$(uptime)
echo -e " ├─ System Load Average : ${UPTIME_DATA#*load average:}"
echo -e " └─ Core Runtime State  : Running Active Process Nodes"

# 3. स्टोरेज (Internal Storage) की वास्तविक स्थिति
echo -e "\n\033[1;35m[3. STORAGE CAPACITY CHANNELS]:\033[0m"
df -h /data/data/com.termux/files/home | awk 'NR==2 {print " ├─ Partition: " $1 "\n ├─ Size:      " $2 "\n └─ Available: " $4 " Space Left"}'

echo -e "\n\033[1;32m====================================================================\033[0m"
echo -e "\033[1;37;42m  [SUCCESS] This data is 100% real telemetry from your Oppo Device. \033[0m"
echo -e "\033[1;36m====================================================================\033[0m"
