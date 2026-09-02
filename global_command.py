import time
from learning_core import JarvisLearningCore
from voice_engine import JarvisVoice
from sensor_hub import SensorHub

class GlobalCommandCenter:
    def __init__(self):
        self.brain = JarvisLearningCore()
        self.vocal = JarvisVoice()
        self.sensors = SensorHub()
        print("--- Global Command Center: ONLINE ---")

    def full_system_init(self):
        self.vocal.speak("Initializing all tactical modules.")
        time.sleep(1)
        
        # Checking environment and learning state
        loc_status = self.sensors.get_location_data()
        memory_state = "Optimized" if self.brain.knowledge_base else "Empty"
        
        print(f"System Check: Sensors [{loc_status}] | Memory [{memory_state}]")
        self.vocal.speak("Global synchronization complete. Waiting for your command.")

if __name__ == "__main__":
    gcc = GlobalCommandCenter()
    gcc.full_system_init()
