import time

class PowerCoreSystem:
    def __init__(self):
        self.energy_level = 100
        self.output_status = "Stable"

    def distribute_power(self, systems_list):
        print("Initiating Power Core: Arc Reactor Status [ACTIVE]")
        time.sleep(1)
        
        for system in systems_list:
            print(f"Routing energy to {system}... [SUCCESS]")
            time.sleep(0.5)
            
        return "Energy distribution complete. All tactical systems online."

if __name__ == "__main__":
    core = PowerCoreSystem()
    sub_systems = ["Flight_Thrusters", "Heads_Up_Display", "Weapon_Systems"]
    print(core.distribute_power(sub_systems))
