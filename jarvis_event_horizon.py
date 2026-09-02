import time

def simulate_future(choice):
    print(f"\n\033[1;36m[SIMULATING]\033[0m Calculating Timeline for: {choice}")
    time.sleep(1.5)
    
    if choice == "LOW_SKILL_JOB":
        outcomes = ["Stagnant Salary", "Limited Growth", "Emotional Regret"]
        color = "\033[1;31m" # Red for Warning
    else:
        outcomes = ["Skill Mastery", "Financial Freedom", "Deepak Protocol Brand"]
        color = "\033[1;32m" # Green for Success
        
    for i, result in enumerate(outcomes, 1):
        print(f" {color}[YEAR {i*2}]\033[0m Result: {result}")
        time.sleep(0.8)

print("\033[1;34m--- JARVIS TEMPORAL SIMULATOR v3.0.5 ---\033[0m")
print("1. Standard ₹9,000 Job")
print("2. The 'Deepak Protocol' (Google Career Path)")

# Let's simulate the winner
simulate_future("DEEPAK_PROTOCOL")

print(f"\n\033[1;35m[VOICE] Deepak... sir, the data is clear. \nIf you choose the hard path today, the \nfuture becomes easy. If you choose the \neasy path today, the future becomes \nimpossible. I have calculated every \nvariable—you are meant for greatness, \nnot for a 9,000 rupee cubicle. Choose wisely.\033[0m")
