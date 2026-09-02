import time

def control_interface(machine_name, mode):
    print(f"\n--- OPTIMUS JARVIS SUPER-FRAME: PHASE 28 ---")
    print(f"[LOG] Attempting Connection with: {machine_name}")
    time.sleep(1.5)
    
    print(f"📡 Status: LINK ESTABLISHED")
    
    if mode == "AUTONOMOUS":
        print(f"🤖 Jarvis Guardian Mode: Taking full control of {machine_name}...")
        return f"SUCCESS: {machine_name} is now navigating via Jarvis Logic."
    elif mode == "MANUAL":
        print(f"🎮 Remote Manual Mode: Handing over controls to User Deepak...")
        return f"SUCCESS: {machine_name} is awaiting manual input via Jarvis HUD."
    else:
        return "ERROR: Mode not recognized."

def run_phase_28():
    # Scenario: Controlling a Pilotless Jet or Drone
    print(control_interface("Drone_Alpha_01", "AUTONOMOUS"))
    time.sleep(1)
    print(control_interface("Mark_1_Exoskeleton", "MANUAL"))
    
    print("\n✅ Phase 28: Remote Machine Control Core Integrated.")

if __name__ == "__main__":
    run_phase_28()
