import time
import random

def atmospheric_manipulation():
    print("\n\033[1;36m[PHASE 2111]: Initializing Atmospheric Manipulation Logic...\033[0m")
    weather_tools = ["Ionized_Cloud_Seeding", "Thermal_Draft_Control", "Lightning_Redirection"]
    for tool in weather_tools:
        time.sleep(0.5)
        print(f">> Calibrating {tool}... \033[1;32mOPTIMAL\033[0m")
    print("\033[1;33m[JARVIS]: Localized weather control is now accessible.\033[0m")

def drone_swarm_intelligence():
    print("\n\033[1;35m[PHASE 2112]: Deploying Micro-Drone Swarm Intelligence...\033[0m")
    swarm_protocols = ["Hive_Mind_Synchronization", "Collision_Avoidance_AI", "Rapid_Reconnaissance"]
    for protocol in swarm_protocols:
        time.sleep(0.5)
        print(f">> Linking {protocol}... \033[1;32mCONNECTED\033[0m")
    
    drone_count = random.randint(500, 1000)
    print(f"\033[1;35m[JARVIS]: {drone_count} Micro-Drones online and awaiting tactical assignment.\033[0m")

if __name__ == "__main__":
    print("="*60)
    print("          OPTIMUS JARVIS SUPER-FRAME: PHASE 2112          ")
    print("="*60)
    atmospheric_manipulation()
    print("-" * 40)
    drone_swarm_intelligence()
    print("\n\033[1;32m[JARVIS]: System Evolution continues. Multi-target control active.\033[0m")
    print("="*60)
