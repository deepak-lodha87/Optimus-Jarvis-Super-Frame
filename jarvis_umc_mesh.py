import time
import json

class UniversalMachineController:
    def __init__(self, unit_id, unit_type):
        self.unit_id = unit_id
        self.unit_type = unit_type
        self.mesh_network = {} # Stores data of other units

    def broadcast_status(self):
        # Unique Logic: Creating a data packet for other units
        status_packet = {
            "id": self.unit_id,
            "type": self.unit_type,
            "coords": [25.21, 75.86], # Example GPS
            "status": "OPERATIONAL"
        }
        print(f"\033[1;34m[{self.unit_id}] Broadcasting Telemetry to Mesh Network...\033[0m")
        return json.dumps(status_packet)

    def receive_and_sync(self, incoming_packet):
        data = json.loads(incoming_packet)
        self.mesh_network[data['id']] = data
        print(f"\033[1;32m[{self.unit_id}] Linked with {data['id']} ({data['type']}). Sync Complete.\033[0m")

    def execute_swarm_task(self):
        if len(self.mesh_network) > 0:
            print(f"\033[1;35m[SWARM] Calculating Collaborative Path for {len(self.mesh_network) + 1} units...\033[0m")
            time.sleep(1)
            return "\033[1;36m[STATUS] All units synchronized. Formation: DELTA-LEAD.\033[0m"
        return "Waiting for peer units..."

if __name__ == "__main__":
    # Simulating two units: A Ground Unit (Bike) and an Aerial Unit (Drone)
    bike = UniversalMachineController("UMC-GROUND-01", "Motorcycle")
    drone = UniversalMachineController("UMC-AERIAL-05", "Drone")
    
    print("-" * 60)
    print("   JARVIS UMC: MULTI-VEHICLE MESH NETWORK (P3223-24)")
    print("-" * 60)
    
    # Machines talking to each other
    packet_from_bike = bike.broadcast_status()
    drone.receive_and_sync(packet_from_bike)
    
    packet_from_drone = drone.broadcast_status()
    bike.receive_and_sync(packet_from_drone)
    
    # Swarm Action
    print("\n" + bike.execute_swarm_task())
    print("-" * 60)
