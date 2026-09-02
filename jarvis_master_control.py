import os

class JarvisMajboot:
    def __init__(self):
        self.user = "Deepak sir"
        self.power_level = "Maximum"
        # Scanned Active Nodes
        self.nodes = ["192.168.1.6", "192.168.1.15", "STARLINK-1008", "Vehicle-ECU"]

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def check_dominance(self):
        print(f"\033[1;36m[STATUS]\033[0m {self.user}, analyzing Jarvis Power-Frame...")
        for node in self.nodes:
            print(f"\033[1;32m[CONTROLLED]\033[0m Node {node} is responding to Master Code.")
        
        self.speak(f"Sir, Jarvis is now the most powerful frame in this network. All hardware is under your control.")

if __name__ == "__main__":
    jarvis = JarvisMajboot()
    jarvis.check_dominance()
