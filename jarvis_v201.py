import os
import time
import random

def morning_motivation():
    quotes = [
        "The best way to predict the future is to create it.",
        "Your only limit is your mind.",
        "Commander, success is a journey, not a destination.",
        "Focus on being productive instead of busy."
    ]
    
    selected_quote = random.choice(quotes)
    print(f"\n[JARVIS]: Good morning, Commander Deepak. Today's insight: {selected_quote}")
    os.system(f"termux-tts-speak '{selected_quote}'")

def daily_diary_log():
    log_entry = input("\n[SYSTEM]: Enter today's progress or thoughts: ")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open("jarvis_diary.txt", "a") as diary:
        diary.write(f"[{timestamp}] - {log_entry}\n")
    
    print("[STATUS]: Progress secured in digital diary.")

def jarvis_main():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 201: PERSONAL INTELLIGENCE    |")
    print("="*50)
    
    morning_motivation()
    daily_diary_log()
    
    print("\n[STATUS]: Intelligence cycle complete.")
    print("="*50)

if __name__ == "__main__":
    jarvis_main()
