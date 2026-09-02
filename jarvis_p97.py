import os
import time
import subprocess

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def diagnostic_scan():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 97 ---")
    print("--- [INITIALIZING ADVANCED DIAGNOSTICS] ---")
    time.sleep(1)

    speak("दीपक, इंटरनल डायग्नोस्टिक स्कैन शुरू हो रहा है।")
    
    # 1. Memory Check
    print("\n[📊] Checking Memory (RAM) Usage...")
    mem_info = subprocess.check_output("free -m", shell=True).decode()
    print(mem_info)
    
    # 2. Uptime Check (System Stability)
    print("[⏱️] Checking System Uptime...")
    uptime = subprocess.check_output("uptime", shell=True).decode()
    print(uptime.strip())

    # 3. Storage Health
    print("[🗄️] Scanning Local Storage Integrity...")
    storage = subprocess.check_output("df -h /data", shell=True).decode()
    print(storage)

    speak("स्कैन पूरा हुआ। आपका सुपर-फ्रेम स्टेबल है और रिस्पॉन्स देने के लिए तैयार है।")
    print("\n✅ Diagnostic Scan: 100% Complete.")

if __name__ == "__main__":
    diagnostic_scan()
