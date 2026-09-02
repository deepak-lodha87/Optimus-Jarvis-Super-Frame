import time, secrets, gc, heapq

class AutonomyMatrix:
    def __init__(self):
        self.agent_id = f"CAM-{secrets.token_hex(4).upper()}"
        self.tasks = []
        self.nodes = [
            (5379, "Goal-Decomp", "BREAKING DOWN MISSION OBJECTIVES..."),
            (5380, "Resource-Scavenge", "PURGING NON-CRITICAL MEMORY SECTORS..."),
            (5381, "Self-Improvement", "REWRITING PERFORMANCE BOTTLENECKS..."),
            (5382, "Priority-Stream", "ALIGNING TASKS WITH USER GOALS..."),
            (5383, "Logic v289", "CAM-CORE: AUTONOMY MATRIX SYNCHRONIZED.")
        ]

    def run_autonomous_loop(self):
        print(f"\033[1;37m--- CORE-AUTONOMY MATRIX ACTIVE (AGENT-ID: {self.agent_id}) ---\033[0m")
        
        colors = [36, 35, 34, 33, 32]
        for i, (p_id, title, status) in enumerate(self.nodes):
            # Simulated Priority Ranking
            priority_score = secrets.randbelow(10) + 1
            heapq.heappush(self.tasks, (priority_score, title))
            
            print(f"\033[1;{colors[i]}m[PRIORITY:{priority_score}/10] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mAUTONOMY STATUS: JARVIS IS NOW OPERATING AS A SELF-GOVERNED AGENT.\033[0m")

if __name__ == "__main__":
    cam = AutonomyMatrix()
    cam.run_autonomous_loop()
