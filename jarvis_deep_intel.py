import os
import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search

class DeepIntel:
    def __init__(self):
        self.master = "Deepak"

    def get_real_info(self, query):
        print(f"\n\033[1;36m[DEEP SCAN]\033[0m Extracting intelligence for: {query}...")
        os.system(f'termux-tts-speak "Analyzing global data for {query}."')
        
        try:
            # गूगल से सबसे भरोसेमंद लिंक ढूंढना
            search_results = list(search(query, num_results=1))
            if not search_results:
                return "Sir, no data found on the uplink."
            
            url = search_results[0]
            # उस वेबसाइट का डेटा पढ़ना (Web Scraping)
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # मुख्य पैराग्राफ से जानकारी निकालना
            paragraphs = soup.find_all('p')
            summary = ""
            for p in paragraphs[:2]: # पहले 2 पैराग्राफ लेना
                if len(p.text) > 50:
                    summary += p.text + " "
            
            if not summary:
                summary = f"Sir, I found a relevant source at {url}, but could not parse text directly."
            
            final_result = summary[:300] # आवाज़ के लिए छोटा सारांश
            print(f"\n\033[1;32m[INTELLIGENCE]:\033[0m {final_result}...")
            os.system(f'termux-tts-speak "{final_result}"')

        except Exception as e:
            print(f"Extraction Error: {e}")
            os.system('termux-tts-speak "Deepak sir, I encountered a firewall issue. Check your connection."')

if __name__ == "__main__":
    intel = DeepIntel()
    user_query = input("Ask Jarvis anything (Deep Scan): ")
    intel.get_real_info(user_query)
