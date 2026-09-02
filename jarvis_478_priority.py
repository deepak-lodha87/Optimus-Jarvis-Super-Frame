# Optimus Jarvis Super-Frame: Phase 477-478
# Feature: Adaptive Priority Logic & Dynamic Task Re-ordering

import time

class JarvisPriority:
    def __init__(self):
        self.code_ver = "478.Adaptive-Priority"
        self.task_list = [
            {"name": "Email_Check", "priority": "LOW"},
            {"name": "Security_Alert", "priority": "CRITICAL"},
            {"name": "Code_Update", "priority": "MEDIUM"}
        ]

    def code_477_analyze_context(self, user_busy):
        print(f"\n[MODULE 477] Checking User Availability: {'BUSY' if user_busy else 'FREE'}")
        time.sleep(1)
        return user_busy

    def code_478_reorder_tasks(self, user_is_busy):
        print("\n[MODULE 478] Re-ordering Task Queue based on Context...")
        time.sleep(1.5)
        
        # If user is busy, only CRITICAL tasks are shown
        if user_is_busy:
            filtered = [t for t in self.task_list if t['priority'] == "CRITICAL"]
            print("[STATUS] Heavy Load/User Busy. Suppressing non-critical tasks.")
        else:
            filtered = sorted(self.task_list, key=lambda x: x['priority'] != "CRITICAL")
            print("[STATUS] User Free. All tasks queued.")

        for task in filtered:
            print(f"[EXECUTING] Task: {task['name']} | Priority: {task['priority']}")

if __name__ == "__main__":
    priority_hub = JarvisPriority()
    print(f"--- {priority_hub.code_ver}: Active ---")
    
    # Simulation 1: User is Busy
    priority_hub.code_477_analyze_context(user_busy=True)
    priority_hub.code_478_reorder_tasks(user_is_busy=True)
    
    print("-" * 30)
    
    # Simulation 2: User is Free
    priority_hub.code_477_analyze_context(user_busy=False)
    priority_hub.code_478_reorder_tasks(user_is_busy=False)
    
    print("\n--- Phase 478 Complete. Jarvis is now Context-Aware. ---")
