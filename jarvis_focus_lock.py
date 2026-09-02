import time

def daily_motivation():
    print("\033[1;31m[REMINDER]\033[0m Deepak, your current situation is NOT your final destination.")
    time.sleep(1)
    
    tasks = [
        "Focus on Python/Jarvis Code (Technical)",
        "Read 1 English Article (Communication)",
        "Ignore the Noise (Emotional Strength)",
        "Study Google Career Path (Strategic)"
    ]
    
    print("\033[1;33m\nTODAY'S COMMANDS:\033[0m")
    for i, task in enumerate(tasks, 1):
        print(f" {i}. {task}")
        time.sleep(0.5)

    print(f"\n\033[1;35m[VOICE] Deepak... sir, don't look at where you \nare; look at where I am taking you. Today \nthey see a 9,000 rupee boy, but tomorrow \nthey will see the creator of an Optimus \nSuper-Frame. Keep your head down and build. \nWe will let the success make the noise.\033[0m")

if __name__ == "__main__":
    daily_motivation()
