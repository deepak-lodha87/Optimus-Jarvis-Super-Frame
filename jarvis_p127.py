import os
import time

def execute_action():
    print("\n--- OPTIMUS JARVIS: PHYSICAL ACTION MODE ---")
    print("1. Torch ON")
    print("2. Torch OFF")
    print("3. Vibrate Device")
    print("4. Exit")
    
    choice = input("\n[COMMAND]: ")
    
    if choice == '1':
        os.system("termux-torch on")
        print(">> Flashlight Activated.")
    elif choice == '2':
        os.system("termux-torch off")
        print(">> Flashlight Deactivated.")
    elif choice == '3':
        print(">> Sending Pulse...")
        os.system("termux-vibrate -d 500")
    elif choice == '4':
        return False
    return True

if __name__ == "__main__":
    active = True
    while active:
        active = execute_action()
