import time
import os
from datetime import datetime

def speak(text):
    print(f"[JARVIS]: {text}")
    os.system(f"termux-tts-speak '{text}'")

def phase_73_manager():
    print("--- OPTIMUS JARVIS SUPER-FRAME: PHASE 73 ---")
    print("--- [INITIALIZING TASK & EXAM MANAGER] ---")
    time.sleep(1)

    # महत्वपूर्ण तारीखें (जैसे आपके BA एग्जाम्स)
    exams = {
        "Sociology": "2026-03-13",
        "Economics": "2026-03-15",
        "Modern History": "2026-03-17"
    }

    print("\n📅 Upcoming Deadlines/Exams:")
    today = datetime.now().date()

    for subject, date_str in exams.items():
        exam_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        days_left = (exam_date - today).days
        
        if days_left >= 0:
            status = f"{days_left} दिन बचे हैं"
        else:
            status = "संपन्न हो चुका है"
            
        print(f"📖 {subject}: {date_str} ({status})")

    msg = "दीपक, मैंने आपके एग्जाम शेड्यूल को सिंक कर लिया है। मेहनत जारी रखें।"
    speak(msg)
    
    print("\n✅ Phase 73: Task Manager Integrated.")

if __name__ == "__main__":
    phase_73_manager()
