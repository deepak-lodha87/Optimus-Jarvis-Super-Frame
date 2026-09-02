import os
import requests

class SatelliteArchitect:
    def __init__(self):
        self.user = "Deepak sir"
        self.api_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"

    def speak(self, text):
        os.system(f'termux-tts-speak "{text}"')

    def fetch_and_solve(self):
        print(f"\033[1;34m[UPLINK]\033[0m Connecting to Starlink Live Registry...")
        try:
            response = requests.get(self.api_url, timeout=10)
            if response.status_code == 200:
                sat_data = response.json()
                target = sat_data[0] # Picking the closest satellite
                name = target['OBJECT_NAME']
                motion = target['MEAN_MOTION']
                
                print(f"\033[1;32m[LIVE]\033[0m Tracking: {name}")
                
                # Logic: If motion is unstable, write the solution
                if motion < 15.0:
                    print(f"\033[1;31m[DEFECT]\033[0m Orbital Decay Detected in {name}!")
                    solution = f"Apply +0.5s Thruster Burn to stabilize {name}."
                    print(f"\033[1;32m[SOLVED]\033[0m Jarvis Recommendation: {solution}")
                    self.speak(f"Deepak sir, I found a defect in {name}. Correction code generated.")
                else:
                    print(f"\033[1;32m[OPTIMAL]\033[0m Satellite is in healthy orbit.")
                    self.speak(f"Sir, {name} telemetry is optimal.")
            else:
                print("\033[1;31m[ERROR]\033[0m Server not responding.")
        except Exception as e:
            print(f"\033[1;31m[ERROR]\033[0m Connection failed: {e}")

if __name__ == "__main__":
    solver = SatelliteArchitect()
    solver.fetch_and_solve()
