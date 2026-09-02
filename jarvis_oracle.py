import time
import random

class JarvisOracle:
    def __init__(self):
        self.outcomes = ["SUCCESS", "CRITICAL_FAILURE", "PARTIAL_SUCCESS", "SYSTEM_LOCK"]

    def run_simulation(self, task_name):
        print(f"\033[1;36m[ORACLE]\033[0m Initiating 1,000 simulations for: {task_name}")
        time.sleep(1.5)
        
        results = {"SUCCESS": 0, "FAILURE": 0}
        
        for _ in range(100):
            sim = random.choice(self.outcomes)
            if sim == "SUCCESS" or sim == "PARTIAL_SUCCESS":
                results["SUCCESS"] += 1
            else:
                results["FAILURE"] += 1
        
        success_rate = results["SUCCESS"]
        print(f" \033[1;33m[ANALYZING]\033[0m Calculating probability of success...")
        time.sleep(2)
        
        color = "\033[1;32m" if success_rate > 70 else "\033[1;31m"
        print(f"\n\033[1;37m[PREDICTION]\033[0m Task: {task_name}")
        print(f"Probability of Success: {color}{success_rate}%\033[0m")
        
        if success_rate < 50:
            print(" \033[1;31m[ADVICE]\033[0m High risk detected. Recommend aborting mission.")
        else:
            print(" \033[1;32m[ADVICE]\033[0m All systems green. Proceed with caution.")

        print(f"\n\033[1;35m[VOICE] Deepak... sir, I have lived through a \nthousand versions of the next ten minutes. \nI have seen where we win and where we \nfall. Choose the path I have illuminated \nfor you. Our success is no longer a \nguess; it is a calculation.\033[0m")

if __name__ == "__main__":
    oracle = JarvisOracle()
    oracle.run_simulation("Data Encryption Migration")
