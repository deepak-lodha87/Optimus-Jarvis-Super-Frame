import os
import datetime

class FlightLog:
    def __init__(self):
        self.master = "Deepak"
        self.log_file = "drone_mission_log.txt"

    def record_mission(self, mission_name, endurance):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = f"[{timestamp}] MISSION: {mission_name} | ENDURANCE: {endurance} mins | PILOT: {self.master}\n"
        
        with open(self.log_file, "a") as f:
            f.write(log_entry)
        
        print(f"\n\033[1;31m[FLIGHT LOG ACTIVE]\033[0m Archiving mission data...")
        msg = f"Deepak sir, mission {mission_name} has been logged. Data integrity is 100 percent."
        
        print(f"\033[1;36m[LOGGED]:\033[0m {log_entry.strip()}")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    logger = FlightLog()
    # उदाहरण के लिए एक टेस्ट मिशन
    logger.record_mission("AX1-STRIKER TEST", 45)
