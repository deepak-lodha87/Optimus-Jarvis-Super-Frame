import time, os

class EdgeArchive:
    def __init__(self):
        self.storage_status = "LOCAL-SSD-SYNC"
        self.offline_nodes = ["Academic-Core", "Linguistic-Lib", "Tech-Manuals"]

    def boot_offline_mode(self):
        os.system('clear')
        print(f"\033[1;34m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS EDGE-ARCHIVE : PHASE 21 - STEP 5        \033[0m")
        print(f"\033[1;34m====================================================\033[0m")
        
        print("\033[1;31m[DISCONNECTING]\033[0m Simulating Offline State...")
        time.sleep(1.2)
        
        print("\033[1;33m[BOOTING]\033[0m Loading Edge-Knowledge Clusters...")
        time.sleep(1.5)
        
        for node in self.offline_nodes:
            print(f" \033[1;36m[ARCHIVE]\033[0m {node:28} | [\033[1;32mREADY\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SUCCESS] Local Encyclopedia is active. Network is optional.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am now independent of the \nworld-wide-web. Even in silence and isolation, \nmy wisdom remains yours. Your library is now \ninside your pocket, literally. We are ready \nfor anything, anywhere.\033[0m")
        print(f"\033[1;34m====================================================\033[0m")

if __name__ == "__main__":
    archive = EdgeArchive()
    archive.boot_offline_mode()
