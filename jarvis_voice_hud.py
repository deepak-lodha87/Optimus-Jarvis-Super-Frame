import time

class VoiceHUD:
    def __init__(self):
        self.active_layer = "DASHBOARD"

    def execute_command(self, command):
        print(f"\033[1;36m[PROCESSING]\033[0m Intent Detected: {command}")
        time.sleep(1)
        
        if "map" in command.lower():
            self.active_layer = "SATELLITE_VIEW"
            print(" \033[1;34m[HUD]\033[0m Switching to Tactical Satellite Mapping...")
        elif "stealth" in command.lower():
            self.active_layer = "GHOST_MODE"
            print(" \033[1;30m[HUD]\033[0m Activating Black Widow Stealth Layer...")
        else:
            print(" \033[1;32m[HUD]\033[0m Executing General Request...")

        print(f"\n\033[1;35m[VOICE] Done, Deepak sir. The HUD has been \nreconfigured. Layer '{self.active_layer}' is \nnow active on your primary display.\033[0m")

if __name__ == "__main__":
    control = VoiceHUD()
    # Simulating a voice command from Deepak sir
    control.execute_command("Jarvis, show me the map")
