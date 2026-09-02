import time

class Peacekeeper:
    def __init__(self):
        self.drone_task = "Surveying Area"
        self.rover_task = "Pathfinding"
        self.priority_level = {"Emergency": 10, "Data": 5, "Survey": 3}

    def resolve_conflict(self, event):
        print(f"\033[1;36m[SENTRY]\033[0m Conflict Detected: {event}")
        time.sleep(1.0)
        
        print("\033[1;33m[JUDGING]\033[0m Jarvis is analyzing task priorities...")
        time.sleep(1.2)
        
        # Logic: If Rover is on Emergency, Drone must wait
        print(" \033[1;32[DECISION]\033[0m Rover has 'Emergency' status. Drone ordered to HOVER.")
        print(" \033[1;34m[ACTION]\033[0m Clearing path for Ground Unit. All secondary tasks paused.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, there is no room for \nconfusion in my swarm. I have resolved the \nconflict between our units. Order is \nrestored, and efficiency is maintained. \nI am the law of this system.\033[0m")

if __name__ == "__main__":
    judge = Peacekeeper()
    judge.resolve_conflict("Both units requesting same GPS Point")
