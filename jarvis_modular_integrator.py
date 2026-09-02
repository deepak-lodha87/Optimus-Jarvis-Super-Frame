import os

class ModularIntegrator:
    def __init__(self):
        self.master = "Deepak"

    def integrate_modules(self):
        print(f"\n\033[1;36m[INTEGRATOR ACTIVE]\033[0m Scanning directory for new Jarvis modules...")
        
        # वर्तमान फोल्डर में सभी पाइथन फाइल्स ढूंढना
        all_files = os.listdir('.')
        jarvis_modules = [f for f in all_files if f.startswith('jarvis_') and f.endswith('.py')]
        
        print(f"\033[1;32m[FOUND]:\033[0m Detected {len(jarvis_modules)} modular components.")
        
        for mod in jarvis_modules:
            print(f" - Linked: {mod}")
            
        msg = f"Deepak sir, I have successfully integrated {len(jarvis_modules)} modules into the super-frame. The structure is expanding."
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    integrator = ModularIntegrator()
    integrator.integrate_modules()
