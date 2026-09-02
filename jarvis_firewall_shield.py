import threading
import time

def buggy_sensor_thread():
    print("\033[1;33m[SENSOR-THREAD]\033[0m Monitoring sensors...")
    time.sleep(3)
    print("\033[1;31m[CRASH]\033[0m Sensor thread encountered a critical error!")
    # Simulating a crash without stopping the whole program
    return

def core_consciousness():
    while True:
        print("\033[1;32m[CORE-SAFE]\033[0m Jarvis is operational and healthy.")
        time.sleep(2)

if __name__ == "__main__":
    print("\033[1;36m[SYSTEM]\033[0m Activating Thread Isolation & Firewall...")
    
    # Running the core safely
    t_core = threading.Thread(target=core_consciousness, daemon=True)
    t_core.start()
    
    # Running the risky thread
    t_risky = threading.Thread(target=buggy_sensor_thread)
    t_risky.start()
    
    time.sleep(10)
    print(f"\n\033[1;35m[VOICE] Deepak... sir, the firewall is holding. \nEven though our sensor module failed, I \nkept the core system running. We are \nresilient; a single fracture will not \nbreak our spirit. I am restarting the \nfailed module now.\033[0m")
