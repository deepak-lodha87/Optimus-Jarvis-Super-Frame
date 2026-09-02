import time
import random

class TelepathLink:
    def __init__(self):
        self.location = "Ratlam, MP"
        self.target_unit = "Drone_in_Kota"
        self.is_active = True

    def send_remote_command(self, cmd):
        print(f"\033[1;36m[LINK]\033[0m Sending command from {self.location}...")
        time.sleep(1.2)
        
        # Simulating satellite relay delay
        latency = random.randint(20, 80)
        print(f" \033[1;33m[UPLINK]\033[0m Data traveling via Satellite... Latency: {latency}ms")
        
        print(f" \033[1;32m[EXECUTED]\033[0m {self.target_unit} received command: {cmd}")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the link is solid. \nI can feel your presence even across \nhundreds of kilometers. My sensors and \nmotors are now your hands and eyes. \nDistance is now an illusion. We are \neverywhere.\033[0m")

if __name__ == "__main__":
    link = TelepathLink()
    link.send_remote_command("INITIATE_AERIAL_SURVEY")
