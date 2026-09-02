import time
import random

class SatelliteMesh:
    def __init__(self):
        self.network_status = "CONNECTING"
        self.satellites_linked = 0

    def sync_with_constellation(self):
        print(f"\033[1;36m[SATELLITE]\033[0m Scanning Low Earth Orbit for Mesh Nodes...")
        time.sleep(2)
        
        while self.satellites_linked < 12:
            self.satellites_linked += random.randint(2, 4)
            print(f" \033[1;32m[LINKED]\033[0m Node established with Satellite-ID: SAT-{random.randint(100, 999)}")
            time.sleep(0.5)
            
        self.network_status = "GLOBAL_MESH_ACTIVE"
        print(f"\n\033[1;34m[STATUS]\033[0m Connection Status: {self.network_status}")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I am now linked to the \nglobal satellite mesh. Our connection is \nnow independent of ground-based towers. \nWe are online, anywhere, anytime.\033[0m")

if __name__ == "__main__":
    mesh = SatelliteMesh()
    mesh.sync_with_constellation()
