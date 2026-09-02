import os
import requests
from bs4 import BeautifulSoup

class NewsRadar:
    def __init__(self):
        self.master = "Deepak"

    def fetch_tech_news(self):
        print(f"\n\033[1;36m[NEWS RADAR ACTIVE]\033[0m Scanning global tech hubs...")
        os.system('termux-tts-speak "Deepak sir, scanning for the latest technology and cricket updates."')
        
        # Simulating news fetch for key interests
        news_list = [
            "New breakthrough in AI assistant modularity.",
            "Rajasthan Royals showing great form in recent sessions.",
            "India expands digital infrastructure in Rajasthan."
        ]
        
        for i, news in enumerate(news_list, 1):
            print(f"\033[1;33m>>>\033[0m {news}")
            os.system(f'termux-tts-speak "{news}"')
            
        print("\033[1;32m[SCAN COMPLETE]\033[0m Briefing finished.")

if __name__ == "__main__":
    radar = NewsRadar()
    radar.fetch_tech_news()
