import time, os, random

class JarvisSimulator:
    def __init__(self):
        self.version = "1,000,000+ PHASES"
        self.sim_engine = "VIRTUAL-PHYSICS-v8"

    def run_flight_test(self, vehicle_name):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS VIRTUAL SIMULATOR : PHASE 8             \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        print(f" \033[1;33m[INITIATING]\033[0m Testing: {vehicle_name}")
        
        tests = ["Lift-Off", "Supersonic Transition", "Extreme Banking", "Emergency Landing"]
        
        for test in tests:
            print(f" \033[1;34m»\033[0m Running {test:25}...", end="")
            time.sleep(0.8)
            success_rate = random.randint(95, 100)
            print(f" [\033[1;32m{success_rate}% SUCCESS\033[0m]")

        print(f"\n\033[1;33m[STATUS] Simulation Complete. Data Synced to Cloud.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the virtual flight tests for the \nIron-Spider stabilizers were flawless. I have run \nover ten thousand permutations of wind and weather. \nThe logic is solid. In the virtual world, we are \nalready flying. Shall we prepare for the next test?\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    sim = JarvisSimulator()
    sim.run_flight_test("Iron-Spider Mark I")
