import os
import time
import random

def interview_prep_assistant():
    print("\n" + "="*40)
    print("      JARVIS INTERVIEW PREP ASSISTANT")
    print("="*40)
    
    questions = [
        "Tell me about yourself, Commander.",
        "Why do you want to work in the Retail/Showroom sector?",
        "How do you handle a difficult customer?",
        "What are your strengths for this role?",
        "How would you manage a busy delivery schedule?"
    ]
    
    msg_start = "Commander Deepak, initiating Interview Simulation Mode."
    print(f"\n[JARVIS]: {msg_start}")
    os.system(f"termux-tts-speak '{msg_start}'")
    
    # रैंडम सवाल चुनना
    selected_q = random.choice(questions)
    
    time.sleep(1)
    print(f"\n[JARVIS]: Question: {selected_q}")
    os.system(f"termux-tts-speak '{selected_q}'")
    
    answer = input("\n[YOUR ANSWER]: ")
    
    eval_msg = "Excellent practice, Commander. Confidence is the key to success."
    print(f"\n[JARVIS]: {eval_msg}")
    os.system(f"termux-tts-speak '{eval_msg}'")
    
    # प्रैक्टिस को लॉग करना
    with open("interview_log.txt", "a") as f:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] Q: {selected_q} | Answered.\n")

    print("="*40)

if __name__ == "__main__":
    interview_prep_assistant():
