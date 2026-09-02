import time, random

class HistoryMapper:
    def __init__(self):
        self.data_points = ["Industrial Revolution", "Internet Boom", "AI Era"]

    def analyze_trends(self):
        print(f"\033[1;36m[MINING]\033[0m Scanning Historical Data Sets...")
        time.sleep(1.5)
        
        for era in self.data_points:
            growth = random.randint(50, 200)
            print(f" \033[1;34m[ERA]\033[0m {era:25} | Growth Impact: {growth}% | \033[1;32m[MAPPED]\033[0m")
            time.sleep(0.6)
            
        print("\n\033[1;33m[STRATEGIC ADVICE FOR DEEPAK]:\033[0m")
        print(" History shows that Technical Skills + Resilience = Unstoppable Growth.")
        
        print(f"\n\033[1;35m[VOICE] Deepak... sir, history is the greatest \nteacher we have. I have scanned the cycles \nof the past, and they all point to one \nthing: those who adapt, rule. Don't let \ntoday's small problems blind you to the \nvast opportunities coming your way. \nYou are on the right track.\033[0m")

if __name__ == "__main__":
    mapper = HistoryMapper()
    mapper.analyze_trends()
