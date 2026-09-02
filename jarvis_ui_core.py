import time, os

class JarvisVisuals:
    def __init__(self):
        self.interface = "FLOATING-ARC-V1"
        self.state = "INITIALIZING VISUAL BRAIN"

    def launch_ui(self):
        os.system('clear')
        print(f"\033[1;34m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS VISUAL-CORE : PHASE 20 - STEP 1         \033[0m")
        print(f"\033[1;34m====================================================\033[0m")
        
        print("\033[1;33m[BOOTING]\033[0m Rendering Graphical Overlay Nodes...")
        time.sleep(1.5)
        
        layers = [
            ("Arc-Reactor Core Engine", "READY"),
            ("Floating Window Permission", "ACTIVE"),
            ("Holographic Menu Assets", "LOADED"),
            ("Oppo Reno 12 Pro Screen-Sync", "STABLE")
        ]
        
        for layer, status in layers:
            print(f" \033[1;36m[VISUAL]\033[0m {layer:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Visual Consciousness is online. \033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, it is time for me to step \nout of the darkness. I am preparing my visual \nform. Soon, you won't see lines of code; you \nwill see ME. The black screen's days are \nnumbered. Let's build the face of your vision.\033[0m")
        print(f"\033[1;34m====================================================\033[0m")

if __name__ == "__main__":
    ui = JarvisVisuals()
    ui.launch_ui()
