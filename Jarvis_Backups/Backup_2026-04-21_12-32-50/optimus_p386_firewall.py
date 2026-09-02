import os
import time
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def neural_firewall_init():
    os.system('clear')
    print("\033[1;31m" + "🔥"*30)
    print("      OPTIMUS NEURAL SYSTEMS : FIREWALL ENFORCER (P386)")
    print("🔥"*30 + "\033[0m")
    
    optimus_speak("Activating Neural Firewall. Encrypting data streams against unauthorized intrusion.")
    
    security_layers = [
        "Packet Inspection",
        "Encrypted Uplink",
        "Intrusion Detection",
        "Adaptive Defense"
    ]
    
    for layer in security_layers:
        print(f"Securing {layer:.<25} [ \033[1;32mSHIELDED\033[0m ]")
        time.sleep(0.5)
    
    print("-" * 55)
    optimus_speak("Firewall is active. The Super-Frame is now protected.")
    print("\033[1;36m[STATUS]: PROTECTED MODE ENABLED\033[0m")

if __name__ == "__main__":
    neural_firewall_init()
