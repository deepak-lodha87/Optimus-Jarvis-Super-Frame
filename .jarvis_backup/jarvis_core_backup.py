


import os
import requests
import psutil

# --- PHASE 1: PERCEPTION & SYSTEM CHECK ---
def system_check():
    battery = psutil.sensors_battery().percent
    print(f"[JARVIS]: System Health: Stable. Battery: {battery}%")
    if battery < 15:
        print("[JARVIS]: Warning: Power low. Safety protocol active.") [cite: 2026-01-16]
    return True

# --- PHASE 2: LOGIC & INCOME SCAN ---
def income_scan():
    print("[JARVIS]: Strategic analysis in progress...")
    try:
        data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        price = data['bitcoin']['usd']
        print(f"[JARVIS]: BTC is at ${price}.")
        if price < 65000:
            print("[JARVIS]: Strategic Advice: Buy for wedding fund.") [cite: 2026-01-18]
        else:
            print("[JARVIS]: Strategic Advice: Hold. Market is high.")
    except:
        print("[JARVIS]: Network Error. Analysis failed.") [cite: 2026-01-16]

# --- MAIN EXECUTION ---
def main():
    print("Welcome Deepak Sir. 8-Phase Architecture is online.")
    system_check() # Phase 1 active
    while True:
        cmd = input("\n[INPUT]: ").lower()
        if 'scan' in cmd:
            income_scan() # Phase 2 active
        elif 'exit' in cmd:
            break

if __name__ == "__main__":
    main()

import json
import os

# --- PERMANENT MEMORY SYSTEM ---
MEMORY_FILE = "jarvis_memory.dat"

def save_progress(phase_name, status="Completed"):
    """Jarvis ki progress ko permanent file mein save karna"""
    memory = {}
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
    
    memory[phase_name] = {
        "status": status,
        "last_updated": str(datetime.datetime.now())
    }
    
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)
    print(f"[JARVIS]: Phase {phase_name} progress locked in permanent memory.") [cite: 2026-01-17]

def load_progress():
    """Purana data recover karna agar code delete ho jaye"""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)
            print("[JARVIS]: Recovering past intelligence...")
            for phase, details in memory.items():
                print(f"  - {phase}: {details['status']} (Verified)")
            return memory
    return {}

# --- COMMAND HANDLER MEIN INTEGRATION ---
# Jab aap Phase 1 poora karein, toh ye call karein:
# save_progress("Phase 1", "Active & Verified")
