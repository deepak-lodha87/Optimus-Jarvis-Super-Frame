import time

class LinkedInTracker:
    def __init__(self):
        self.platform = "LinkedIn"
        self.project = "Optimus Jarvis Super-Frame"

    def analyze_wait_time(self, hours_passed):
        print(f"\n\033[1;36m[SYSTEM ANALYSIS]\033[0m Monitoring {self.platform} Reach...")
        time.sleep(1)
        
        if hours_passed < 24:
            status = "Early Stage (Gathering Data)"
            advice = "Patience is Paramount. Focus on your BA Final Year studies while I monitor."
        else:
            status = "Active Stage"
            advice = "Consider engaging with more tech communities to boost visibility."
            
        print(f"\033[1;32m[STATUS]\033[0m {status}")
        print(f"\033[1;34m[ADVICE]\033[0m {advice}")

if __name__ == "__main__":
    tracker = LinkedInTracker()
    tracker.analyze_wait_time(13) # आपकी स्थिति: 13 घंटे
