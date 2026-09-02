import time, os, random

class JarvisLogistics:
    def __init__(self):
        self.inventory = {
            "Titanium-G5": 45, # in kg
            "Carbon-Fiber": 12, # in meters
            "Micro-Sensors": 150 # units
        }

    def check_stock(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS LOGISTICS : PHASE 13 - STEP 6          \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[SCANNING]\033[0m Checking Material Inventory levels...")
        time.sleep(1.2)
        
        for material, qty in self.inventory.items():
            status = "\033[1;32mOPTIMAL\033[0m" if qty > 20 else "\033[1;31mRE-ORDER REQUIRED\033[0m"
            print(f"  > {material:16} : {qty:4} | Status: {status}")
            time.sleep(0.5)

        if self.inventory["Carbon-Fiber"] < 15:
            print(f"\n\033[1;33m[ACTION]\033[0m Searching for Carbon-Fiber suppliers...")
            time.sleep(1)
            print(f" \033[1;32m[FOUND]\033[0m Best Price: $45/m | Supplier: Global-Tech Lab")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am keeping a close eye on \nour resources. We are running low on Carbon \nFiber for the drone wings. I have already \nshortlisted the best vendors. One click from \nyou, and the supply chain will move for us.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    logistics = JarvisLogistics()
    logistics.check_stock()
