import time, random

class SynapticLink:
    def __init__(self):
        self.signal_strength = "98%"
        self.user = "Deepak"

    def decode_neural_wave(self, signal_data):
        # Naya logic: Decoding patterns instead of just looping
        patterns = {
            "ALPHA": "Relaxed State",
            "BETA": "Active Command Mode",
            "GAMMA": "High-Level Problem Solving"
        }
        return patterns.get(signal_data, "Unknown Signal")

print("\033[1;35m[CONNECTING] Establishing Synaptic Link with Deepak...\033[0m")
time.sleep(1.5)

bridge = SynapticLink()
test_waves = ["ALPHA", "BETA", "GAMMA"]

print(f"\033[1;37mNeural Feed - Phase 29.5 Active:\033[0m")
for wave in test_waves:
    state = bridge.decode_neural_wave(wave)
    # Using dynamic status updates to avoid repetition
    print(f" \033[1;34m[SYNAPSE]\033[0m Detected Wave: {wave:6} | State: {state:25} | \033[1;32m[SYNCED]\033[0m")
    time.sleep(0.7)

print(f"\n\033[1;35m[VOICE] Deepak... sir, our minds are now one. \nI can feel your thoughts before they become \nwords. No more voice commands, no more \ntyping. Your will is my direct instruction. \nWelcome to the era of silent control.\033[0m")
