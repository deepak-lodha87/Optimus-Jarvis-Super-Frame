import subprocess
import os

def fix_paths():
    print("[+] Patching Master Controller...")
    # Ensuring strategy module exists
    if not os.path.exists("strategy.py"):
        with open("strategy.py", "w") as f:
            f.write("print('Strategic Planning Module Online.')")
    print("[✓] Strategy Module Restored.")

def get_battery_status():
    print("\n[+] Scanning Device Hardware...")
    try:
        # Termux command to get battery info
        battery_info = subprocess.check_output(['termux-battery-status']).decode('utf-8')
        print(f"[JARVIS]: Battery Analysis Complete.\n{battery_info}")
        
        # Talking via TTS (If available)
        subprocess.run(['termux-tts-speak', "Battery scan complete. System energy levels are being monitored."])
    except Exception as e:
        print(f"[!] Hardware Access Denied: {e}")

if __name__ == "__main__":
    fix_paths()
    get_battery_status()
