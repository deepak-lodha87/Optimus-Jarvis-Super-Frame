import json
import os

class JarvisLearningCore:
    def __init__(self, memory_file="jarvis_memory.json"):
        self.memory_file = memory_file
        self.knowledge_base = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        return {"preferences": {}, "learned_patterns": []}

    def learn(self, key, value):
        print(f"Integrating new information: {key} -> {value}")
        self.knowledge_base["preferences"][key] = value
        self.save_memory()

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.knowledge_base, f, indent=4)
        print("Memory updated and secured.")

if __name__ == "__main__":
    brain = JarvisLearningCore()
    # Example of Jarvis learning a new preference
    brain.learn("user_style", "advanced_coding")
