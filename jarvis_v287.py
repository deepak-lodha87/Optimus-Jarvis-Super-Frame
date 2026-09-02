import time, random

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def dynamic_response():
    greetings = ["Systems are nominal, Commander.", "Always a pleasure to assist you.", "Ready for the next phase of development."]
    
    print(f"\n{C['B']}[JARVIS]: Interactive Session Active. Type 'exit' to stop.{C['W']}")
    
    while True:
        user_input = input(f"{C['G']}Commander: {C['W']}").lower()
        
        if "exit" in user_input or "quit" in user_input:
            print(f"{C['Y']}Jarvis: Going back to standby mode.{C['W']}")
            break
        elif "status" in user_input:
            print(f"{C['Y']}Jarvis: {random.choice(greetings)}{C['W']}")
        elif "starhawk" in user_input:
            print(f"{C['Y']}Jarvis: The Starhawk flight dynamics are optimized and ready for testing.{C['W']}")
        else:
            print(f"{C['Y']}Jarvis: Protocol acknowledged. Proceeding with command...{C['W']}")

def mission_entry():
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'DYNAMIC INTERACTION PROTOCOL':^42} {C['B']}║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    dynamic_response()

if __name__ == "__main__":
    mission_entry()
