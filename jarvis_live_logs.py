import time
import os

def show_logs():
    print(f"\n\033[1;36m[SYSTEM MONITOR]\033[0m Initializing Live Log Stream for Deepak sir...")
    time.sleep(1)
    
    logs = [
        "Uplink Established", "Handshake: SECURE", "Remote Node: CONNECTED", "Auth: SUCCESS"
    ]
    
    print("\n\033[1;37mTIME        | EVENT              | STATUS\033[0m")
    print("------------|--------------------|---------")
    
    for log in logs:
        timestamp = time.strftime("%H:%M:%S")
        print(f"{timestamp}    | {log.ljust(18)} | \033[1;32m[OK]\033[0m")
        time.sleep(0.5)

    msg = "Deepak sir, your live surveillance log is ready. Every command is being monitored."
    os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    show_logs()
