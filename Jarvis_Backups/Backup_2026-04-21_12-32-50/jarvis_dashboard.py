import os
import time

def clear_screen():
    os.system('clear')

def display_dashboard():
    clear_screen()
    print("\033[1;33m" + "="*50)
    print("      OPTIMUS JARVIS SUPER-FRAME : MASTER TRACKER")
    print("="*50 + "\033[0m")
    
    completed_phases = {
        "Phase 1": "Perception & Core Logic",
        "Phase 2": "Hardware Integration (Oppo Reno 12 Pro)",
        "Phase 3009-3051": "Singularity Core & Tactical Defense",
        "Phase 3052": "Neural Feedback Loop (Active)"
    }
    
    upcoming_phases = [
        "Phase 3053: Advanced Encryption Barrier",
        "Phase 3054: Autonomous Decision Matrix",
        "Phase 3055: Global Blueprint Database"
    ]

    print("\033[1;32m[✓] COMPLETED MILESTONES:\033[0m")
    for p, desc in completed_phases.items():
        print(f"  • {p}: {desc}")
        time.sleep(0.1)

    print("\n\033[1;34m[>] UPCOMING OBJECTIVES:\033[0m")
    for up in upcoming_phases:
        print(f"  • {up}")
        time.sleep(0.1)

    print("\n\033[1;33m" + "="*50)
    print(f" SYSTEM STATUS: ONLINE | USER: DEEPAK | V2.5")
    print("="*50 + "\033[0m")

if __name__ == "__main__":
    display_dashboard()
