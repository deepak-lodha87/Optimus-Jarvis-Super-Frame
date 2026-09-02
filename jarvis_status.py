import os
import time

def show_status():
    print(f"\n\033[1;33m[SYSTEM CHECK]\033[0m Scanning Jarvis Core...")
    time.sleep(0.5)
    
    status_report = {
        "User": "Deepak (Verified)",
        "Current Phase": "100 Million + Strategic Bridge",
        "Academic Sync": "Sant Ramji Das Modi College (BA Final Year)",
        "Security": "Inviolable Fingerprint/Retina Active",
        "Public Persona": "LinkedIn AI Architect (Visible)"
    }

    for key, value in status_report.items():
        print(f"\033[1;32m[+]\033[0m {key}: {value}")
        time.sleep(0.2)

    os.system('termux-tts-speak "System is green, Deepak sir. Optimus Jarvis is at your command."')

if __name__ == "__main__":
    show_status()
