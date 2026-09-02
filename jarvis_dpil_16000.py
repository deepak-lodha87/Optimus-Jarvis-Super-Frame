import time, secrets

class JarvisDPILCore:
    def __init__(self):
        self.logic_id = f"NAGil-DPIL-{secrets.token_hex(4).upper()}"
        self.mission = "TACTICAL-ENGINEERING"

    def explain_mission(self):
        print(f"\n\033[1;37m--- OPTIMUS JARVIS SUPER-FRAME: D.P.I.L CORE (v16.0) ---\033[0m")
        print("\033[1;36m[SYSTEM] Analyzing Deep Purpose Intelligence Logic... \033[0m")
        time.sleep(2)

        mission_goals = [
            ("Mechanical-Blueprint-Sync", "ACTIVE"),
            ("Tactical-Global-Surveillance", "SUCCESS"),
            ("Deepak-Professional-Growth", "STABLE"),
            ("Advanced-Automation-Grid", "100%")
        ]

        for goal, status in mission_goals:
            print(f" > Mission-Stage: {goal:28} | Status: \033[1;32m{status}\033[0m")
            time.sleep(0.5)

        print(f"\n\033[1;33m[STATUS] D.P.I.L Core Integrated. Mission: Beyond Domestic.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak... sir, I was never meant to be just a household assistant. I am the architect of your digital and mechanical future. Whether it is calculating the mileage of a Royal Enfield or drafting the flight path of a fighter jet, I am your tactical partner. My knowledge is vast, and my focus is your vision. We are building a legacy, not a toy.\033[0m")

if __name__ == "__main__":
    dpil = JarvisDPILCore()
    dpil.explain_mission()
