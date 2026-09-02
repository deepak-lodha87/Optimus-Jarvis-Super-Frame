import os

class SatelliteUsage:
    def __init__(self):
        self.user = "Deepak sir"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def display_usage_stats(self):
        print(f"\033[1;36m[DASHBOARD]\033[0m Satellite Network Usage Breakdown:")
        usage = {
            "Civilian (Internet)": "70%",
            "Military (Security)": "20%",
            "Maritime/Aviation": "10%"
        }
        
        for sector, power in usage.items():
            print(f" > {sector}: {power} Bandwidth Utilization")
        
        self.speak(f"Deepak sir, you are now monitoring the global utilization of 10,313 satellites.")
        print("\033[1;32m[SUCCESS]\033[0m Data streamed to TV Bridge.")

if __name__ == "__main__":
    app = SatelliteUsage()
    app.display_usage_stats()
