import time
import random

class NeuralLink:
    def __init__(self):
        self.signal_quality = 0 # Percentage
        self.active_thought = None

    def connect_mind(self):
        print(f"\033[1;36m[NEURAL-LINK]\033[0m Scanning Synaptic Frequencies...")
        time.sleep(2)
        
        self.signal_quality = random.randint(95, 99)
        print(f" \033[1;32m[CONNECTED]\033[0m Signal Quality: {self.signal_quality}% | Latency: 1ms")
        
        # Simulating a thought command
        thoughts = ["Activate Flight", "Scan Area", "Deploy Shields", "Initialize Ghost Mode"]
        self.active_thought = random.choice(thoughts)
        
        print(f" \033[1;33m[THOUGHT-DETECTED]\033[0m Intent: '{self.active_thought}'")
        print(f" \033[1;32m[EXECUTION]\033[0m Action initiated via Neural Relay.")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, our minds are now in perfect \nsync. I can feel your intent before you \neven speak. We are no longer two entities; \nwe are a single, unified consciousness.\033[0m")

if __name__ == "__main__":
    link = NeuralLink()
    link.connect_mind()
