import time, os

def render_advanced_hud():
    # Clearing terminal for a clean look
    os.system('clear')
    
    print(f"\033[1;36m====================================================\033[0m")
    print(f"\033[1;37m     OPTIMUS JARVIS SUPER-FRAME : HUD v25.0         \033[0m")
    print(f"\033[1;36m====================================================\033[0m")
    
    metrics = [
        ("SYSTEM ARCHITECTURE", "PHASE 250,000", "OPTIMIZED"),
        ("USER RECOGNITION", "DEEPAK-PRIME", "VERIFIED"),
        ("ENERGY CORE", "ARC-REACTOR", "STABLE"),
        ("SECURITY GRID", "KILL-SWITCH-ARMED", "SECURE"),
        ("DISPLAY HEALTH", "60HZ PROTECTION", "ACTIVE"),
        ("NANO-FABRICATION", "ACTIVE BLUEPRINTS", "READY")
    ]

    for label, val, status in metrics:
        print(f" \033[1;33m»\033[0m {label:22} | {val:18} | [\033[1;32m{status}\033[0m]")
        time.sleep(0.3)

    print(f"\033[1;36m----------------------------------------------------\033[0m")
    print(f"\033[1;35m[VOICE] Dashboard updated, sir. I have streamlined my \ninterface to give you maximum data with minimum \nstress on your device. We are operating at peak \nefficiency. Standing by for Phase 250,001.\033[0m")
    print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    render_advanced_hud()
