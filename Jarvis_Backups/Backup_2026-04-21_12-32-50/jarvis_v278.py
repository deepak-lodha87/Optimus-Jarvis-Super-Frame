import os, time
from datetime import datetime

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def get_battery_info():
    # Termux के जरिए बैटरी स्टेटस चेक करने का कमांड
    try:
        if os.path.exists('/sys/class/power_supply/battery/capacity'):
            with open('/sys/class/power_supply/battery/capacity', 'r') as f:
                cap = f.read().strip()
            with open('/sys/class/power_supply/battery/status', 'r') as f:
                stat = f.read().strip()
            return f"{cap}%", stat
        else:
            return "N/A", "Unknown"
    except:
        return "N/A", "Unknown"

def mission_entry():
    level, status = get_battery_info()
    now = datetime.now().strftime("%H:%M")
    
    # Sensor Interface HUD
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS SENSOR LINK ACTIVE':^42} {C['B']}║")
    print(f"╠" + "═"*44 + "╣")
    print(f"║ {C['W']}POWER LEVEL: {C['G']}{level:<6}{C['W']} | STATUS: {C['G']}{status:<1

cat << 'EOF' > jarvis_v278.py
import os, time
from datetime import datetime

C = {"G": "\033[92m", "B": "\033[96m", "Y": "\033[93m", "R": "\033[91m", "W": "\033[0m", "BOLD": "\033[1m"}

def get_battery_info():
    # Termux के जरिए बैटरी स्टेटस चेक करने का कमांड
    try:
        if os.path.exists('/sys/class/power_supply/battery/capacity'):
            with open('/sys/class/power_supply/battery/capacity', 'r') as f:
                cap = f.read().strip()
            with open('/sys/class/power_supply/battery/status', 'r') as f:
                stat = f.read().strip()
            return f"{cap}%", stat
        else:
            return "N/A", "Unknown"
    except:
        return "N/A", "Unknown"

def mission_entry():
    level, status = get_battery_info()
    now = datetime.now().strftime("%H:%M")
    
    # Sensor Interface HUD
    print(f"{C['B']}╔" + "═"*44 + "╗")
    print(f"║ {C['BOLD']}{'JARVIS SENSOR LINK ACTIVE':^42} {C['B']}║")
    print(f"╠" + "═"*44 + "╣")
    print(f"║ {C['W']}POWER LEVEL: {C['G']}{level:<6}{C['W']} | STATUS: {C['G']}{status:<10} {C['B']:>2} ║")
    print(f"║ {C['W']}SYNC TIME: {now:^10} | MODULE: V-278 {C['B']:>10} ║")
    print(f"╠" + "═"*44 + "╣")
    print(f"║ {C['Y']}SENSORS DETECTED: [BATTERY], [THERMAL]{C['B']:>6} ║")
    print(f"╚" + "═"*44 + f"╝{C['W']}")
    
    print(f"\n{C['B']}[JARVIS]: Monitoring device vitals in real-time.{C['W']}")

if __name__ == "__main__":
    mission_entry()
