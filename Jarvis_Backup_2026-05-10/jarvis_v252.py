import os
import random
import time

def strategic_motivation_engine():
    print("\n" + "="*45)
    print("      JARVIS STRATEGIC MOTIVATION")
    print("="*45)
    
    # आपके पिछले प्रोजेक्ट्स और प्रयासों के आधार पर प्रेरणा
    quotes = [
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Commander, your progress on the Optimus Frame is statistically impressive.",
        "Precision in code leads to perfection in execution. Keep going, Deepak.",
        "The best way to predict the future is to create it, one phase at a time."
    ]
    
    selected_quote = random.choice(quotes)
    
    msg = f"Commander Deepak, I have analyzed your trajectory. {selected_quote}"
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")
    
    print("\n" + "="*45)

if __name__ == "__main__":
    strategic_motivation_engine()
