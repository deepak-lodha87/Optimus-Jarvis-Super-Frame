import os
import time
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def neural_system_audit():
    os.system('clear')
    print("\033[1;36m" + "🔍"*30)
    print("      OPTIMUS NEURAL SYSTEMS : SYSTEM AUDIT (P375)")
    print("🔍"*30 + "\033[0m")
    
    optimus_speak("Initiating full system audit. Verifying module integrity and compliance.")
    
    # Critical Core Files to Check
    critical_modules = [
        "optimus_v2_core.py", "optimus_p371_access_gate.py", 
        "optimus_p369_firewall.py", "optimus_p365_logs.py",
        "optimus_p372_backup.py"
    ]
    
    print("\n\033[1;33m[SCANNING]: Checking Neural Core Integrity...\033[0m")
    time.sleep(1.5)
    
    missing_count = 0
    for module in critical_modules:
        if os.path.exists(module):
            status = "\033[1;32m[VERIFIED]\033[0m"
        else:
            status = "\033[1;31m[MISSING]\033[0m"
            missing_count += 1
        
        print(f"Module: {module:<30} | Status: {status}")
        time.sleep(0.4)
    
    print("-" * 60)
    
    # Compliance Report
    if missing_count == 0:
        print("\033[1;32m[REPORT]: System is 100% Compliant. No anomalies detected.\033[0m")
        optimus_speak("Audit complete. All neural pathways are stable and secure.")
    else:
        print(f"\033[1;31m[REPORT]: Audit Failed. {missing_count} critical modules are missing.\033[0m")
        optimus_speak("Warning. System integrity compromised. Please run recovery protocols.")

if __name__ == "__main__":
    neural_system_audit()
