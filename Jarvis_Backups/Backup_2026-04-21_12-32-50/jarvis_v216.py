import os
import time
import subprocess

def network_speed_monitor():
    print("\n" + "="*40)
    print("      JARVIS NETWORK SPEED MONITOR")
    print="*40)
    
    msg_start = "Commander Deepak, initiating network speed analysis..."
    print(f"\n[JARVIS]: {msg_start}")
    os.system(f"termux-tts-speak '{msg_start}'")
    
    print("[PROCESS]: Pinging global servers...")
    time.sleep(1.5)
    
    try:
        # एक सामान्य पिंग टेस्ट (Google DNS पर)
        response = subprocess.getoutput("ping -c 4 8.8.8.8")
        
        if "time=" in response:
            # पिंग समय निकालना
            ping_time = response.split("time=")[1].split(" ")[0]
            status_msg = f"Network is stable. Latency is {ping_time} milliseconds."
            print(f"\n[SUCCESS]: {status_msg}")
            os.system(f"termux-tts-speak '{status_msg}'")
        else:
            error_msg = "Commander, connection is unstable or offline."
            print(f"\n[ALERT]: {error_msg}")
            os.system(f"termux-tts-speak '{error_msg}'")
            
    except Exception as e:
        print(f"[ERROR]: Analysis failed. {e}")

    print("="*40)

if __name__ == "__main__":
    network_speed_monitor()
