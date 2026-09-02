import time
import random

def run_advanced_diagnostics():
    print("\n\033[1;36m[SYSTEM]: Initializing Phase 2101 - Advanced Diagnostic Scan...\033[0m")
    components = ["Memory_Core", "Database_Integrity", "Interface_Link", "Protocol_Shield"]
    
    for comp in components:
        time.sleep(0.4)
        status = "\033[1;32mOPTIMAL\033[0m"
        print(f"Checking {comp}... Status: {status}")
    print("\033[1;33m[JARVIS]: Diagnostic Complete. System Health at 100%.\033[0m")

def initialize_neural_interface():
    print("\n\033[1;35m[SYSTEM]: Activating Neural Signal Interface Framework...\033[0m")
    print(">> Syncing Brain-Computer Interface (BCI) protocols...")
    
    signals = ["Alpha", "Beta", "Theta", "Gamma"]
    for signal in signals:
        time.sleep(0.5)
        strength = random.randint(85, 99)
        print(f">> Signal [{signal}]: {strength}% Connectivity Established.")
    
    print("\n\033[1;32m[JARVIS]: Neural link is stable. Ready for command input.\033[0m")

if __name__ == "__main__":
    print("="*60)
    print("          OPTIMUS JARVIS SUPER-FRAME: PHASE 2101          ")
    print("="*60)
    run_advanced_diagnostics()
    print("-" * 40)
    initialize_neural_interface()
    print("="*60)
