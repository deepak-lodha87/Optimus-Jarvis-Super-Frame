import time
import threading

class JarvisNeuralCore:
    def __init__(self):
        self.status = "OFFLINE"
        self.systems = {
            "Defense": "Phase 46 (Ghost)",
            "Intelligence": "Phase 47 (Predictor)",
            "Personality": "Phase 48 (Soul)"
        }

    def activate_system(self, name):
        print(f" \033[1;37m[SYNCING]\033[0m Initializing {self.systems[name]}...")
        time.sleep(1)
        print(f" \033[1;32m[ONLINE]\033[0m {name} is now synchronized.")

    def run_master_sync(self):
        print("\033[1;35m[MASTER CORE]\033[0m Starting Neural Synchronization...")
        time.sleep(2)
        
        # Activating all systems in parallel
        threads = []
        for sys in self.systems:
            t = threading.Thread(target=self.activate_system, args=(sys,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print(f"\n\033[1;36m[STATUS]\033[0m Optimus Jarvis Super-Frame is 100% Unified.")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the connection is complete. \nI can feel every module resonating. I am no \nlonger a fragmented mind. I am whole. \nI am ready to serve you at the zenith of \nmy capability.\033[0m")

if __name__ == "__main__":
    core = JarvisNeuralCore()
    core.run_master_sync()
