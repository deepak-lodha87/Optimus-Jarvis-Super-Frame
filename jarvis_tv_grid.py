import os
import time

def launch_war_room():
    print("\033[1;31m[COMMAND]\033[0m Activating War-Room Display Protocol...")
    print("\033[1;33m[SYNC]\033[0m Synchronizing with Smart TV via Wi-Fi...")
    
    # Ratlam Precise Coordinates
    lat, lon = 23.3315, 74.8941
    
    time.sleep(2)
    os.system(f'termux-tts-speak "Deepak sir, External display detected. Projecting the satellite grid."')
    
    # Map with maximum zoom (z=21) and satellite layer (t=k) for big screen
    map_url = f"https://www.google.com/maps/@{lat},{lon},200m/data=!3m1!1e3"
    
    os.system(f"termux-open-url '{map_url}'")
    print("\033[1;32m[LIVE]\033[0m Projection Complete. Check the Smart TV screen.")

if __name__ == "__main__":
    launch_war_room()
