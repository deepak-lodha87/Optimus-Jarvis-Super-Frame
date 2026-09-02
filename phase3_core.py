import time

def execute_command(command):
    print(f"\n[SYSTEM]: Accessing Phase 3 Automation Protocols...")
    time.sleep(1)
    print(f"[ACTION]: Executing '{command}'...")
    
    # Simulating hardware/software control
    for i in range(1, 4):
        print(f"  > Processing Task {i}/3...")
        time.sleep(0.5)
    
    print(f"[SUCCESS]: Command '{command}' has been fully executed.")

if __name__ == "__main__":
    print("--- Optimus Jarvis Phase 3: Automation & Control ---")
    user_cmd = "Initialize Suit Blueprints & Jet Propulsion Systems"
    execute_command(user_cmd)
