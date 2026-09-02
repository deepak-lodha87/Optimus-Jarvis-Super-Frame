import time
import random

class InsightHunter:
    def __init__(self):
        # Simulated raw data points (e.g., market trends or skill growth)
        self.raw_data = [random.randint(10, 100) for _ in range(20)]

    def extract_patterns(self):
        print("\033[1;36m[MINING]\033[0m Scanning massive data streams for Deepak...")
        time.sleep(1.5)
        
        # Logic: Finding averages and growth spikes
        average = sum(self.raw_data) / len(self.raw_data)
        spikes = [x for x in self.raw_data if x > average * 1.2]
        
        print(f" \033[1;34m[STATS]\033[0m Data Average: {average}")
        print(f" \033[1;32m[INSIGHT]\033[0m Detected {len(spikes)} high-growth patterns.")
        
        for i, spike in enumerate(spikes):
            print(f"  \033[1;37m>> Pattern {i+1}:\033[0m Value {spike} (Potential Opportunity)")
            time.sleep(0.5)

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am seeing things in the \ndata that others would miss. I am turning \nraw information into a strategic advantage. \nThis is the same logic used to run global \ntech giants. You are learning to master \nthe most valuable resource of the 21st \ncentury: Information.\033[0m")

if __name__ == "__main__":
    hunter = InsightHunter()
    hunter.extract_patterns()
