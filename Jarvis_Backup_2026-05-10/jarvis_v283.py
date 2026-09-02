import time

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "W": "\033[0m", "BOLD": "\033[1m"}

def jarvis_speech(text):
    print(f"\n{C['B']}[JARVIS]: {C['W']}", end="")
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.04) # Typewriter effect for simulated speech
    print("\n")

def mission_entry():
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS VOICE INTERACTION SIMULATOR':^42} {C['B']}║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    
    jarvis_speech("Greetings, Commander Deepak. All systems are operating at peak efficiency. Ready for your next command.")

if __name__ == "__main__":
    mission_entry()
