import time, os

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def neural_voice():
    os.system('clear')
    print(f"{C['B']}╔" + "═"*48 + "╗")
    print(f"║ {C['BOLD']}{'NEURAL VOICE INTERFACE v299':^46} {C['B']}║")
    print(f"╚" + "═"*48 + f"╝{C['W']}")
    
    responses = {
        "hello": "Greetings, Commander Deepak. All systems are online.",
        "status": "Core integrity is at 100%. All modules are stable.",
        "starhawk": "Starhawk flight systems are optimized for deployment.",
        "repair": "Deep repair protocol is on standby mode.",
        "identity": "I am Optimus Jarvis, your personal AI framework."
    }

    print(f"\n{C['BOLD']}{C['Y']}--- VOICE INPUT SIMULATED ---{C['W']}")
    
    while True:
        try:
            user_input = input(f"\n{C['G']}Commander Deepak: {C['W']}").lower()
            if 'exit' in user_input or 'quit' in user_input:
                print(f"\n{C['Y']}[JARVIS]: Hibernating...{C['W']}")
                break
            
            print(f"{C['B']}Analyzing patterns...{C['W']}")
            time.sleep(0.8)
            
            matched = False
            for key in responses:
                if key in user_input:
                    print(f"\n{C['BOLD']}{C['B']}[JARVIS]: {responses[key]}{C['W']}")
                    matched = True
                    break
            
            if not matched:
                print(f"\n{C['R']}[JARVIS]: Pattern not found.{C['W']}")
        except EOFError:
            break

if __name__ == "__main__":
    try:
        neural_voice()
    except KeyboardInterrupt:
        print(f"\n{C['R']}[ALERT]: Interrupted.{C['W']}")
