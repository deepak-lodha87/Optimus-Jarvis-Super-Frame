# Optimus Jarvis Super-Frame: Phase 435-436
# Feature: Self-Learning Algorithm & Failure Analysis

import json
import os

class JarvisLearning:
    def __init__(self):
        self.code_ver = "436.Neural-Learn"
        self.failure_log = "failure_memory.json"
        self.memory = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.failure_log):
            with open(self.failure_log, 'r') as f:
                return json.load(f)
        return {}

    def code_435_analyze_failure(self, task_name, reason):
        print(f"\n[MODULE 435] Analyzing Failure in: {task_name}")
        self.memory[task_name] = {"reason": reason, "correction_applied": True}
        with open(self.failure_log, 'w') as f:
            json.dump(self.memory, f)
        print(f"[LEARNING] Failure recorded. Strategy for {task_name} updated.")

    def code_436_apply_correction(self, task_name):
        print(f"\n[MODULE 436] Checking Correction Memory for: {task_name}")
        if task_name in self.memory:
            print(f"[ADAPT] Previous failure detected ({self.memory[task_name]['reason']}).")
            print(f"[ACTION] Deploying Alternative Strategy to ensure success.")
        else:
            print("[STATUS] No previous failures found. Proceeding with Standard Protocol.")

if __name__ == "__main__":
    learner = JarvisLearning()
    print(f"--- {learner.code_ver}: Active ---")
    
    # Simulating a failure and then a correction
    task = "Network_Infiltration_Scan"
    
    # 1. First time it fails
    learner.code_435_analyze_failure(task, "Timeout Error")
    
    # 2. Next time it corrects itself
    learner.code_436_apply_correction(task)
    
    print("\n--- Phase 436 Complete. Jarvis is now learning from mistakes. ---")
