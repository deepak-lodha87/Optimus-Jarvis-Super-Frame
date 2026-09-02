import time

def web_shooter_logic(pressure_level):
    print("\n--- OPTIMUS JARVIS SUPER-FRAME: PHASE 30 ---")
    print(f"[LOG] Analyzing Web-Fluid Pressure: {pressure_level} PSI")
    time.sleep(1)

    if pressure_level < 300:
        return "🕸️ MODE: Thin Strand (For stealth or swinging)."
    elif 300 <= pressure_level <= 700:
        return "🕸️ MODE: Standard Web (For capturing targets)."
    elif pressure_level > 700:
        return "💥 MODE: Web Grenade (High-impact restraint)."
    else:
        return "⚠️ WARNING: Pressure unstable."

def run_phase_30():
    print("[LOG] Testing Web-Shooter Nozzle Calibration...")
    
    # Test 1: Low pressure for swinging
    print(web_shooter_logic(250))
    
    # Test 2: High pressure for combat
    print(web_shooter_logic(850))

    print("\n✅ Phase 30: Web-Shooter Pressure Logic Integrated.")

if __name__ == "__main__":
    run_phase_30()
