import os
import time
import psutil

def resource_optimizer():
    print("\n" + "="*40)
    print("      JARVIS RESOURCE OPTIMIZER")
    print("="*40)
    
    msg_init = "Commander Deepak, analyzing system resource distribution..."
    print(f"\n[JARVIS]: {msg_init}")
    os.system(f"termux-tts-speak '{msg_init}'")
    
    # RAM उपयोग की जाँच
    ram = psutil.virtual_memory()
    ram_usage = ram.percent
    
    print(f"\n[ANALYSIS]: Current RAM Usage: {ram_usage}%")
    
    if ram_usage > 80:
        alert = "Commander, RAM usage is critically high. Optimization recommended."
        print(f"[ALERT]: {alert}")
        os.system(f"termux-tts-speak '{alert}'")
        
        print("\n[SUGGESTIONS]:")
        print("1. Close unused Termux sessions.")
        print("2. Clear system cache.")
        print("3. Terminate non-essential background tasks.")
    else:
        success = "System resources are within optimal parameters."
        print(f"[STATUS]: {success}")
        os.system(f"termux-tts-speak '{success}'")

    time.sleep(1)
    print("\n" + "="*40)

if __name__ == "__main__":
    resource_optimizer()
