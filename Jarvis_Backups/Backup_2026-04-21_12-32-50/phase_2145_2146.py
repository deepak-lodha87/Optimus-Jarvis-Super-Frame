import time
import random

def deploy_advanced_layer(phase, protocols):
    print(f"\033[1;35m[SYSTEM]: Deploying {phase}...\033[0m")
    for protocol in protocols:
        time.sleep(0.5)
        print(f"[*] Activating {protocol}... \033[1;32mSUCCESS\033[0m")
    print("-" * 50)

# Phase 2145: Nano-Repair & Self-Healing
deploy_advanced_layer("PHASE 2145: NANO-REPAIR & SELF-HEALING", [
    "Sub-Atomic_Structure_Repair",
    "Auto_Reconfiguration_Core",
    "Energy_Leak_Sealing"
])

# Phase 2146: Adaptive Cyber-Defense
deploy_advanced_layer("PHASE 2146: ADAPTIVE CYBER-DEFENSE", [
    "Firewall_Morphing_Algorithm",
    "Encrypted_Ghost_Node",
    "Intrusion_Counter_Strike"
])

health_check = random.choice(["100% Optimized", "System: Flawless", "No Damage Detected"])

print(f"\n\033[1;34m[JARVIS]: Health Status: {health_check}.\033[0m")
print(f"\033[1;32m[JARVIS]: The system can now repair itself and adapt to any attack.\033[0m")
print("=" * 60)
