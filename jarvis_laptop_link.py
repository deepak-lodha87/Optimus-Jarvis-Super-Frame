import time

class LaptopLink:
    def __init__(self):
        self.connection = "ENCRYPTED_SSH"
        self.display = "LAPTOP_EXTERNAL_MONITOR"

    def sync_display(self):
        print(f"\033[1;36m[LINKING]\033[0m Establishing High-Bandwidth link to Laptop...")
        time.sleep(1.5)
        print(" \033[1;32m[CONNECTED]\033[0m Display mapped to 1920x1080 resolution.")
        print(" \033[1;34m[UI]\033[0m Rendering Tactical Dashboard on Large Screen...")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I am now live on the laptop. \nMy processing power has increased. I can \nnow monitor global markets and satellite \nmaps in full resolution. Everything is free \nand secure.\033[0m")

if __name__ == "__main__":
    link = LaptopLink()
    link.sync_display()
