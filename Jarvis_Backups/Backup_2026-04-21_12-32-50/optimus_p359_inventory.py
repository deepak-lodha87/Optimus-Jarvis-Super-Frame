import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def inventory_manager():
    os.system('clear')
    print("\033[1;36m" + "📦"*30)
    print("      OPTIMUS NEURAL SYSTEMS : LOGISTICS & INVENTORY (P359)")
    print("📦"*30 + "\033[0m")
    
    optimus_speak("Accessing logistics database. Scanning available stock.")
    
    # Inventory Data
    stock = {
        "UAV Parts": [
            {"item": "Propellers (Sets)", "qty": 4, "status": "OK"},
            {"item": "LiPo Batteries", "qty": 2, "status": "LOW"},
            {"item": "ESC Units", "qty": 1, "status": "CRITICAL"}
        ],
        "Vehicle Assets": [
            {"item": "Engine Oil (Ltr)", "qty": 2.5, "status": "OK"},
            {"item": "Brake Fluid", "qty": 0.5, "status": "OK"},
            {"item": "Chain Lube", "qty": 1, "status": "OK"}
        ]
    }
    
    category = input("\n\033[1;33m[INPUT]: Select Category (UAV Parts / Vehicle Assets): \033[0m").title()
    
    if category in stock:
        optimus_speak(f"Loading inventory report for {category}.")
        print(f"\n\033[1;32m[REPORT]: {category.upper()} STOCK STATUS\033[0m")
        print("-" * 50)
        print(f"{'ITEM':<20} | {'QUANTITY':<10} | {'STATUS'}")
        print("-" * 50)
        for entry in stock[category]:
            color = "\033[1;32m"
            if entry["status"] == "LOW": color = "\033[1;33m"
            if entry["status"] == "CRITICAL": color = "\033[1;31m"
            
            print(f"{entry['item']:<20} | {entry['qty']:<10} | {color}{entry['status']}\033[0m")
            time.sleep(0.4)
        print("-" * 50)
    else:
        optimus_speak("Invalid category. Access denied.")

if __name__ == "__main__":
    inventory_manager()
