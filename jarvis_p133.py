import os
import socket

def check_connection():
    try:
        # Checking connection to Google's DNS
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

def hybrid_engine():
    print("\n" + "="*50)
    print("|    JARVIS PHASE 133: HYBRID CONNECTIVITY       |")
    print("="*50)

    if check_connection():
        mode = "ONLINE MODE (Full Global Access)"
        status_msg = "Commander, we are connected. I can access live data."
    else:
        mode = "OFFLINE MODE (Local Database Only)"
        status_msg = "Internet unavailable. Switching to offline vault."

    print(f"\n[SYSTEM STATUS]: {mode}")
    print(f"[JARVIS]: {status_msg}")
    os.system(f"termux-tts-speak '{status_msg}'")

    # Future Integration: Fetching live vs local blueprints
    print("\n[LOG]: Ready for Phase 134: Aerodynamics Simulation.")

if __name__ == "__main__":
    hybrid_engine()
