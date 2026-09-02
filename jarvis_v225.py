import os
import time
import random

def academic_quiz_protocol():
    print("\n" + "="*40)
    print("      JARVIS ACADEMIC QUIZ CORE")
    print("="*40)
    
    msg_start = "Commander Deepak, initiating rapid-fire academic review."
    print(f"\n[JARVIS]: {msg_start}")
    os.system(f"termux-tts-speak '{msg_start}'")
    
    # आपके विषयों से संबंधित सैंपल सवाल
    questions = {
        "Sociology": "Who is known as the father of Sociology?",
        "Economics": "What is the basic law of supply and demand?",
        "History": "In which year did the First War of Indian Independence occur?"
    }
    
    subject, question = random.choice(list(questions.items()))
    
    print(f"\n[SUBJECT]: {subject}")
    print(f"[QUESTION]: {question}")
    os.system(f"termux-tts-speak 'Subject {subject}. {question}'")
    
    answer = input("\n[YOUR ANSWER]: ")
    
    feedback = "Record updated. Continuous learning is the hallmark of a Commander."
    print(f"\n[JARVIS]: {feedback}")
    os.system(f"termux-tts-speak '{feedback}'")
    
    # क्विज़ सेशन को लॉग करना
    with open("study_log.txt", "a") as f:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] Quiz on {subject} completed.\n")

    print("\n" + "="*40)

if __name__ == "__main__":
    academic_quiz_protocol()
