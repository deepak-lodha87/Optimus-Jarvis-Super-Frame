import time

class JarvisAutomator:
    def __init__(self):
        self.user = "Deepak"
        self.skill_set = "AI Developer & Service Expert"

    def draft_job_application(self, company_name):
        print(f"\033[1;36m[AUTOMATING]\033[0m Drafting application for {company_name}...")
        time.sleep(2)
        
        draft = f"""
        Subject: Application for Innovative Role - {self.user}
        
        Dear Hiring Team at {company_name},
        
        I am a versatile developer who has built the 'Optimus Jarvis Super-Frame'
        exclusively on a mobile device. My background as an Exemplary Service 
        Advisor, combined with 50 phases of AI development, makes me a unique 
        candidate for your team.
        """
        
        print("\n\033[1;32m[DRAFT COMPLETED]\033[0m Review the professional output below:")
        print(f"\033[1;37m{draft}\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak sir, the draft is ready. It is sharp, \nprofessional, and reflects your true authority. \nShall I prepare the next task?\033[0m")

if __name__ == "__main__":
    automator = JarvisAutomator()
    automator.draft_job_application("Google")
