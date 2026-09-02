import os
import json
import time

class OmniDashboard:
    def __init__(self):
        self.master = "Deepak"
        self.modules = ["master_blueprints.json", "nano_biomech_vault.json", "defense_protocols_v900.json"]

    def initialize_dashboard(self):
        print(f"\n\033[1;37;44m [ OPTIMUS JARVIS : OMNI-CONTROL DASHBOARD ] \033[0m")
        print(f"\033[1;36mScanning all active sectors...\033[0m")
        
        found_modules = []
        for module in self.modules:
            if os.path.exists(module):
                found_modules.append(module)
                print(f"\033[1;32m[✓]\033[0m {module} Loaded.")
            else:
                print(f"\033[1;31m[X]\033[0m {module} Not Found.")

        # Real-time System Analytics
        status = "CRITICAL" if len(found_modules) == 0 else "OPTIMAL"
        
        report = (
            f"Deepak sir, the Omni-Dashboard is now governing all integrated protocols. "
            f"System status is {status}. Ready to execute high-level blueprints."
        )

        print("-" * 50)
        print(f"| MASTER STATUS : ONLINE")
        print(f"| ACTIVE SECTORS: {len(found_modules)}")
        print(f"| CORE STATE    : {status}")
        print("-" * 50)

        os.system(f'termux-tts-speak "{report}"')

    def list_blueprints(self):
        if os.path.exists("master_blueprints.json"):
            with open("master_blueprints.json", "r") as f:
                data = json.load(f)
                print("\033[1;33mAvailable Blueprints:\033[0m", list(data.keys()))

if __name__ == "__main__":
    jarvis = OmniDashboard()
    jarvis.initialize_dashboard()
    jarvis.list_blueprints()
