import time

class BlueprintArchive:
    def __init__(self):
        self.archive = {
            "Iron-Man-MK3": "Power: Arc Reactor, Armor: Gold-Titanium Alloy",
            "Fighter-Jet-F22": "Engine: Twin F119-PW-100, Stealth: Active",
            "Drone-Tactical": "Control: AI-Neural Link, Range: 500km"
        }

    def access_blueprint(self, model):
        print(f"\033[1;33m[DECRYPTING]\033[0m Accessing classified blueprints for {model}...")
        time.sleep(2)
        if model in self.archive:
            print(f"\033[1;32m[DATA FOUND]\033[0m Specs: {self.archive[model]}")
        else:
            print("\033[1;31m[ERROR]\033[0m Model not in database, sir.")

if __name__ == "__main__":
    jarvis_data = BlueprintArchive()
    jarvis_data.access_blueprint("Iron-Man-MK3")
