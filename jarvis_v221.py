import os
import time
from datetime import datetime

def academic_countdown_oracle():
    print("\n" + "="*40)
    print("      JARVIS ACADEMIC COUNTDOWN")
    print("="*40)
    
    # लक्ष्य की तारीख (उदाहरण के लिए रिव्यु की तारीख)
    target_date = datetime(2026, 4, 6, 10, 0, 0)
    now = datetime.now()
    
    remaining = target_date - now
    
    msg_init = "Commander Deepak, analyzing your academic timeline..."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    if remaining.total_seconds() > 0:
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        
        status = f"Commander, you have {days} days and {hours} hours remaining until the next milestone."
        print(f"\n[COUNTDOWN]: {status}")
        os.system(f"termux-tts-speak '{status}'")
    else:
        overdue = "Commander, the scheduled milestone has already passed."
        print(f"\n[ALERT]: {overdue}")
        os.system(f"termux-tts-speak '{overdue}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    academic_countdown_oracle()
