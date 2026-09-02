import os
import time
import random

def daily_motivation_hub():
    print("\n" + "="*40)
    print("      JARVIS DAILY MOTIVATION HUB")
    print("="*40)
    
    # प्रेरणादायक विचारों का संग्रह
    quotes = [
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Your time is limited, so don't waste it living someone else's life.",
        "The only way to do great work is to love what you do.",
        "Believe you can and you're halfway there.",
        "Commander, excellence is not a skill, it is an attitude."
    ]
    
    msg_init = "Commander Deepak, retrieving today's source of inspiration..."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    time.sleep(1.5)
    
    # रैंडम मोटिवेशनल कोट चुनना
    selected_quote = random.choice(quotes)
    
    print(f"\n[INSIGHT]: {selected_quote}")
    os.system(f"termux-tts-speak '{selected_quote}'")
    
    print("\n" + "="*40)

if __name__ == "__main__":
    daily_motivation_hub()
