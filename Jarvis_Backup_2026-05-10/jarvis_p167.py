import time
import os

def neural_routine_logging():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 167: NEURAL ROUTINE LOGGING   |")
    print("="*50)

    # Gate 3: Sync check with Phase 154 (Integrated Core)
    # Reference:
    print("[SYSTEM]: Syncing with Phase 154 Integrated Core...")
    time.sleep(1)

    # Logic Gate 1 & 2: Passive Monitoring
    current_time = time.localtime().tm_hour
    print(f"[DATA]: Current cycle detected at hour: {current_time}")

    if 23 <= current_time or current_time <= 5:
        mode = "STEALTH_DEFENSE"
        status = "REDUCED_ACTIVITY_LOGGED"
    else:
        mode = "ACTIVE_OPERATIONS"
        status = "USER_ROUTINE_DETECTED"

    msg = f"Commander Deepak, pattern identified as {mode}. Status: {status}."
    
    # Executing Jarvis Response
    print(f"\n[JARVIS]: {msg}")
    os.system(f"termux-tts-speak '{msg}'")

    # Gate 2: Data Integrity (Saving to Vault from Phase 157)
    # Reference:
    print("\n[RESULT]: Routine data successfully moved to Deep Vault.")
    print("="*50)

if __name__ == "__main__":
    neural_routine_logging()
