import time

class StrategicJarvis:
    def __init__(self):
        self.user = "Deepak"
        self.phase = "3009"
        # Strategic Thresholds
        self.critical_temp = 100
        self.low_fuel = 15

    def analyze_situation(self, temp, fuel, rpm):
        print(f"\033[1;35m>> PHASE {self.phase}: RUNNING STRATEGIC ANALYSIS <<\033[0m")
        time.sleep(1)
        
        print(f"[STATUS] Engine: {temp}C | Fuel: {fuel}% | RPM: {rpm}")
        
        # Decision Making Logic
        if temp >= self.critical_temp:
            print("\033[1;31m[STRATEGY] Critical Overheat! Advice: Stop vehicle and check coolant level.\033[0m")
        elif fuel <= self.low_fuel:
            print("\033[1;33m[STRATEGY] Low Fuel. Navigating to nearest gas station based on coordinates.\033[0m")
        elif rpm > 4000:
            print("\033[1;34m[STRATEGY] High Performance Mode detected. Monitoring oil pressure for stability.\033[0m")
        else:
            print("\033[1;32m[STRATEGY] All systems optimal. Maintain current velocity, Sir.\033[0m")

    def boot(self):
        print(f"\033[1;36m>> GOOD MORNING, ARCHITECT {self.user}. SYSTEM ONLINE. <<\033[0m")
        # Simulating a real-world scenario
        self.analyze_situation(temp=102, fuel=12, rpm=850)

if __name__ == "__main__":
    brain = StrategicJarvis()
    brain.boot()
