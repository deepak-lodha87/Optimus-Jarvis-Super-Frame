import os
import time
from googlesearch import search

class GlobalIntel:
    def __init__(self):
        self.master = "Deepak"

    def fetch_latest_info(self, query):
        print(f"\n\033[1;36m[UPLINK]\033[0m Searching global database for: {query}...")
        os.system(f'termux-tts-speak "Searching the web for {query}, Deepak sir."')
        
        try:
            # इंटरनेट से टॉप 1 रिजल्ट निकालना
            results = list(search(query, num_results=1))
            if results:
                info = f"Deepak sir, according to the latest data, the information for {query} is available at this link: {results[0]}"
                print(f"\033[1;32m[RESULT]:\033[0m {results[0]}")
                os.system(f'termux-tts-speak "{info}"')
            else:
                os.system('termux-tts-speak "Sorry sir, I could not find current information on that."')
        except Exception as e:
            print(f"Connection Error: {e}")
            os.system('termux-tts-speak "Sir, please check your internet connection."')

if __name__ == "__main__":
    intel = GlobalIntel()
    # अब यह वॉयस कमांड से भी जुड़ सकता है
    query = input("Ask Jarvis anything: ")
    intel.fetch_latest_info(query)
