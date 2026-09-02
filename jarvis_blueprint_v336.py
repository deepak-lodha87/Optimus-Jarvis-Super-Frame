import json

# Database for Vehicles and Drones
blueprints = {
    "Hunter 350": {
        "Engine": "349cc, Single cylinder, 4-stroke",
        "Power": "20.2 bhp @ 6100 rpm",
        "Torque": "27 Nm @ 4000 rpm",
        "Top Speed": "114 kmph",
        "Blueprint_ID": "RE-H350-B01"
    },
    "UAV Drone": {
        "Type": "Quadceptor",
        "Flight Controller": "Pixhawk 4",
        "Battery": "5000mAh LiPo",
        "Range": "2km",
        "Blueprint_ID": "DRN-OPT-V1"
    }
}

def get_blueprint(item_name):
    data = blueprints.get(item_name)
    if data:
        print(f"\033[1;36m[DATA FOUND]: {item_name} Specs\033[0m")
        for key, value in data.items():
            print(f"| {key}: {value}")
    else:
        print("\033[1;31m[ERROR]: No blueprint found for " + item_name + "\033[0m")

if __name__ == "__main__":
    item = input("Enter asset name (Hunter 350 / UAV Drone): ")
    get_blueprint(item)
