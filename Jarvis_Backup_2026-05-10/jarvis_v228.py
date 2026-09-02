import os
import time
import random

def news_oracle_protocol():
    print("\n" + "="*40)
    print("      JARVIS NEWS & KNOWLEDGE ORACLE")
    print("="*40)
    
    msg_init = "Commander Deepak, accessing global news archives and knowledge database."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    # सिमुलेटेड न्यूज़ और फैक्ट्स
    news_feed = [
        "Tech: AI framework developments have reached a new milestone today.",
        "Space: New discovery found in the deep sectors of the Mars surface.",
        "Sports: Rajasthan Royals are showing a dominant form in the current season.",
        "Knowledge: Did you know? Python was named after the comedy group Monty Python."
    ]
    
    time.sleep(1.5)
    selected_news = random.choice(news_feed)
    
    report = f"Flash Update: {selected_news}"
    print(f"\n[REPORT]: {report}")
    os.system(f"termux-tts-speak '{report}'")
    
    success = "Information feed synchronized. Standing by for further instructions."
    print(f"\n[JARVIS]: {success}")
    os.system(f"termux-tts-speak '{success}'")

    print("\n" + "="*40)

if __name__ == "__main__":
    news_oracle_protocol()
