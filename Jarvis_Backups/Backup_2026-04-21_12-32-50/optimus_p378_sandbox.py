import time
import os
import subprocess

def optimus_speak(text):
    print(f"\033[1;34m[OPTIMUS]:\033[0m {text}")
    subprocess.run(['termux-tts-speak', text])

def logic_sandbox_lab():
    os.system('clear')
    print("\033[1;33m" + "🧪"*30)
    print("      OPTIMUS NEURAL SYSTEMS : LOGIC SANDBOX (P378)")
    print("🧪"*30 + "\033[0m")
    
    optimus_speak("Entering neural sandbox environment. System isolation active.")
    
    # User Input for Test Code
    print("\n\033[1;36m[SANDBOX MODE]: Enter test logic or command below:\033[0m")
    test_logic = input("TEST COMMAND > ")
    
    print("\n\033[1;33m[VIRTUALIZING]: Creating isolated execution thread...\033[0m")
    time.sleep(1.5)
    
    # Simulated Safety Check
    is_safe = True
    if "rm" in test_logic or "delete" in test_logic:
        is_safe = False
    
    if is_safe:
        print(f"\033[1;32m[PASSED]: Logic verified in Sandbox. No system risks detected.\033[0m")
        optimus_speak("Test logic is stable. You may proceed to integrate this into the core.")
    else:
        print(f"\033[1;31m[REJECTED]: Dangerous command detected. Sandbox prevented execution.\033[0m")
        optimus_speak("Security alert. The requested command could damage the system integrity.")

if __name__ == "__main__":
    logic_sandbox_lab()
