import os
import time
from datetime import datetime, timedelta

def project_deadline_sync():
    print("\n" + "="*40)
    print("      JARVIS GLOBAL DEADLINE TRACKER")
    print("="*40)
    
    msg_init = "Commander Deepak, synchronizing project timelines and global clocks."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    # मुख्य प्रोजेक्ट्स और उनकी डेडलाइन्स
    projects = {
        "Optimus Framework Next Phase": datetime(2026, 4, 15),
        "Academic Final Submission": datetime(2026, 4, 10),
        "Career Portfolio Update": datetime(2026, 4, 5)
    }
    
    now = datetime.now()
    
    print("\n[PROJECT STATUS]:")
    for project, deadline in projects.items():
        remaining = deadline - now
        days_left = remaining.days
        
        status_msg = f"{project}: {days_left} days remaining."
        print(f"- {status_msg}")
        
        if days_left < 3:
            alert = f"Urgent attention required for {project}!"
            print(f"  [ALERT]: {alert}")
            os.system(f"termux-tts-speak '{alert}'")
    
    time.sleep(1)
    
    summary = "Commander, your project schedule is synchronized. No immediate conflicts detected."
    print(f"\n[JARVIS]: {summary}")
    os.system(f"termux-tts-speak '{summary}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    project_deadline_sync()
