import time
import random
import os

def system_self_diagnosis():
    print("\n" + "-"*30)
    print("[DIAGNOSTICS]: Running Full System Check...")
    time.sleep(1)
    systems = ["Uplink", "Navigation", "Stealth", "Intelligence"]
    for sys in systems:
        status = "ONLINE" if random.random() > 0.1 else "LATENCY DETECTED"
        print(f" -> {sys} System: {status}")
        time.sleep(0.5)
    print("[RESULT]: System integrity at 98.4%. Ready for deployment.")
    print("-"*30 + "\n")

def stealth_ghost_protocol():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 181: STEALTH & GHOST    |")
    print("="*50)
    cloak_status = ["THERMAL_MASKING", "RADAR_ABSORPTION", "CLOAK_ACTIVE"]
    current_mode = random.choice(cloak_status)
    print(f"[SYSTEM]: Initializing {current_mode}...")
    time.sleep(1.5)
    signature_reduction = random.randint(90, 99)
    print(f"[JARVIS LOGIC]: Signature reduced by {signature_reduction}%.")
    stealth_msg = "Commander Deepak, Ghost Protocol is active. We are now invisible."
    print(f"\n[JARVIS]: {stealth_msg}")
    # Termux TTS (अगर API इंस्टॉल है)
    os.system(f"termux-tts-speak '{stealth_msg}'")
    print("="*50)

if __name__ == "__main__":
    print("[SYSTEM]: Connecting to Optimus Jarvis Intelligence Matrix...")
    time.sleep(1.2)
    print("[STATUS]: Neural links synchronized.")
    system_self_diagnosis()
    stealth_ghost_protocol()
