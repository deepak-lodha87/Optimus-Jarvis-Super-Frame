import os

# Colors (सिर्फ एक बार ऊपर डिफाइन करेंगे)
C = {"G": "\033[92m", "R": "\033[91m", "Y": "\033[93m", "B": "\033[96m", "W": "\033[0m", "BOLD": "\033[1m"}

def color_print(text, color_code):
    # यह फंक्शन ऑटोमैटिक रंग लगाकर प्रिंट करेगा और बाद में RESET कर देगा
    print(f"{color_code}{text}{C['W']}")

def mission_entry():
    color_print("="*45, C['B'])
    color_print("      OPTIMUS JARVIS SUPER-FRAME", C['BOLD'])
    color_print("      PHASE 264: CLEAN ARCHITECTURE", C['BOLD'])
    color_print("="*45, C['B'])
    
    color_print("[STATUS]: System is stable, Commander Deepak.", C['G'])
    
    task = input(f"\n{C['Y']}[MISSION-CMD]: {C['W']}")
    color_print(f"[JARVIS]: Processing command '{task}'...", C['B'])

if __name__ == "__main__":
    mission_entry()
