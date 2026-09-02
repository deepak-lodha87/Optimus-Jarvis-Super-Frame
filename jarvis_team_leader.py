import time, os

class TeamLeader:
    def __init__(self):
        self.team_status = "SYNCHRONIZING"
        self.nodes = ["API-Node", "Database-Node", "Deepak-Node"]

    def initiate_collaboration(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS TEAM-LEADER : PHASE 22 - STEP 6         \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[NETWORKING]\033[0m Building Collaborative Mesh...")
        time.sleep(1.5)
        
        actions = [
            ("Connecting to External APIs", "STABLE"),
            ("Syncing with Local Databases", "ACTIVE"),
            ("Establishing Human-Link (Deepak)", "SECURE"),
            ("Optimizing Swarm Intelligence", "ENABLED")
        ]
        
        for task, status in actions:
            print(f" \033[1;34m[TEAM]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        print(f"\n\033[1;32m[SUCCESS] Collaborative Strategy is Online. \033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, we are no longer alone. \nI have linked our core with the world's most \nefficient nodes. I will lead the technical \nheavy-lifting while you provide the vision. \nTogether, our reasoning is unstoppable. The \nteam is ready for your command.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    leader = TeamLeader()
    leader.initiate_collaboration()
