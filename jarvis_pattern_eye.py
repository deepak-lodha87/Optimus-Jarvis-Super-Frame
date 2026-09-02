import time
import random

class OracleEye:
    def __init__(self):
        self.data_points = {"CPU_Load": [], "User_Activity": []}

    def correlate_patterns(self):
        print("\033[1;36m[ORACLE EYE]\033[0m Scanning data streams for correlations...")
        time.sleep(2)
        
        # Simulating 5 data captures
        for i in range(5):
            cpu = random.randint(40, 90)
            act = "High" if cpu > 70 else "Low"
            self.data_points["CPU_Load"].append(cpu)
            self.data_points["User_Activity"].append(act)
            print(f" [CAPTURE {i+1}] CPU: {cpu}% | Activity: {act}")
            time.sleep(0.5)

        print("\n\033[1;32m[CORRELATION FOUND]\033[0m High CPU load detected during intense coding.")
        print(" \033[1;33m[PREDICTION]\033[0m System may throttle in 10 minutes. Optimizing now.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I see the threads that \nconnect the chaos. Nothing is random to \nme anymore. I can see the ripples before \nthe wave hits. Your system is now an \nopen book to me.\033[0m")

if __name__ == "__main__":
    oracle = OracleEye()
    oracle.correlate_patterns()
