import os
import time

def activate_alien_sniffer():
    os.system('clear')
    print("\033[1;31m[EXTRATERRESTRIAL SCAN]\033[0m Activating Deep-Space Signal Sniffer...")
    
    # Scanning high-frequency bands
    print("\033[1;33m[SCANNING]\033[0m Searching for Non-Human Tech Signatures...")
    time.sleep(2)
    
    os.system('termux-tts-speak "Deepak sir, scanning for unidentified aerial phenomena signatures. Strategic database is being updated."')
    
    print("\n\033[1;32m[SYSTEM READY]\033[0m")
    print("Status: Monitoring 'Hidden' Satellite Data")
    print("Difference: Scanning beyond human-made frequencies.")

if __name__ == "__main__":
    activate_alien_sniffer()
