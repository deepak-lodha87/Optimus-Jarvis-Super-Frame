import os
import json
import datetime

class CognitiveMemory:
    def __init__(self):
        self.master = "Deepak"
        self.memory_file = "jarvis_long_term_memory.json"
        self.load_memory()

    def load_memory(self):
        if not os.path.exists(self.memory_file):
            self.memory = {"knowledge_base": [], "last_update": ""}
        else:
            with open(self.memory_file, "r") as f:
                self.memory = json.load(f)

    def save_knowledge(self, topic, detail):
        entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "topic": topic,
            "detail": detail
        }
        self.memory["knowledge_base"].append(entry)
        self.memory["last_update"] = entry["timestamp"]
        
        with open(self.memory_file, "w") as f:
            json.dump(self.memory, f, indent=4)
            
        print(f"\n\033[1;32m[MEMORY OPTIMIZED]:\033[0m {topic} archived in long-term memory.")
        os.system(f'termux-tts-speak "Deepak sir, I have committed {topic} to my cognitive memory."')

if __name__ == "__main__":
    brain = CognitiveMemory()
    # उदाहरण: जार्विस को कुछ नया सिखाना
    brain.save_knowledge("Project_Alpha", "Integration of Mach 2.0 propulsion logic.")
