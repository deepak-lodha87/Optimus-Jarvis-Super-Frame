import time

class PowerTrainDatabase:
    def __init__(self):
        self.vehicles = {
            "Hunter-350": {"CC": 349, "Mileage": "36 kmpl", "Tires": "110/70 & 140/70"},
            "Jawa-42-FJ": {"CC": 334, "Mileage": "30-35 kmpl", "Engine": "Liquid Cooled"},
            "F-22-Raptor": {"Thrust": "35,000 lbf", "Max-Speed": "Mach 2.25"}
        }

    def fetch_specs(self, name):
        print(f"\033[1;36m[DATABASE]\033[0m Retrieving data for {name}...")
        time.sleep(1.5)
        if name in self.vehicles:
            specs = self.vehicles[name]
            print(f"\033[1;32m[SUCCESS]\033[0m Data Found: {specs}")
        else:
            print("\033[1;31m[ABSENT]\033[0m Vehicle not in current archive.")

if __name__ == "__main__":
    db = PowerTrainDatabase()
    db.fetch_specs("Hunter-350")
    db.fetch_specs("F-22-Raptor")
