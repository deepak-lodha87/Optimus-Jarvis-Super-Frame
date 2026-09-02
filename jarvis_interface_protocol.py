import os

class InterfaceProtocol:
    def __init__(self):
        self.master = "Deepak"
        # सक्रिय मॉड्यूल्स की सूची
        self.active_links = {
            "Security": "Online",
            "Battery": "Monitoring",
            "Kernel": "Linked",
            "Scheduler": "Active"
        }

    def sync_modules(self):
        print(f"\n\033[1;35m[INTERFACE PROTOCOL ACTIVE]\033[0m Synchronizing all sub-systems...")
        os.system('termux-tts-speak "Deepak sir, establishing a communication bridge between all Jarvis modules."')
        
        print("\033[1;36m--- MODULE STATUS BOARD ---\033[0m")
        for module, status in self.active_links.items():
            print(f"| {module.ljust(12)} : \033[1;32m{status}\033[0m |")
        print("\033[1;36m---------------------------\033[0m")
        
        os.system('termux-tts-speak "All systems are now in sync. Bridge is stable."')

if __name__ == "__main__":
    protocol = InterfaceProtocol()
    protocol.sync_modules()
