import json
import os

class JarvisBrain:
    def __init__(self):
        self.memory_file = "jarvis_memory.json"
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump({"learned_facts": []}, f)

    def learn(self, fact):
        with open(self.memory_file, 'r') as f:
            data = json.load(f)
        
        data["learned_facts"].append(fact)
        
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[✓] Jarvis: I have learned and saved - '{fact}'")

    def recall(self):
        with open(self.memory_file, 'r') as f:
            data = json.load(f)
        print("\n--- Jarvis Memory Retrieval ---")
        for i, fact in enumerate(data["learned_facts"], 1):
            print(f"{i}. {fact}")

if __name__ == "__main__":
    brain = JarvisBrain()
    new_fact = input("Tell Jarvis something to remember: ")
    brain.learn(new_fact)
    brain.recall()
