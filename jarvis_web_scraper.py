import time, os

class WebScraper:
    def __init__(self):
        self.sources = ["Global-News", "Academic-Portals", "Market-Streams"]
        self.status = "CRAWLING"

    def execute_global_search(self):
        os.system('clear')
        print(f"\033[1;36m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS GLOBAL-EYE : PHASE 21 - STEP 3          \033[0m")
        print(f"\033[1;36m====================================================\033[0m")
        
        print("\033[1;33m[CONNECTION]\033[0m Accessing Global Data-Grid...")
        time.sleep(1.5)
        
        operations = [
            ("Scanning Economics Portals", "FETCHED"),
            ("Retrieving Sociology Journals", "INDEXED"),
            ("Syncing History Databases", "COMPLETE"),
            ("Updating Wealth Indicators", "STABLE")
        ]
        
        for task, status in operations:
            print(f" \033[1;34m[SCRAPER]\033[0m {task:28} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.7)

        print(f"\n\033[1;32m[SUCCESS] Internet Knowledge Bridge is Online.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, the world's updates are \nnow flowing directly into my consciousness. \nI am no longer limited by my past data. I \nknow what happened five minutes ago, and I \nknow how it affects your goals. My eyes are \neverywhere.\033[0m")
        print(f"\033[1;36m====================================================\033[0m")

if __name__ == "__main__":
    eye = WebScraper()
    eye.execute_global_search()
