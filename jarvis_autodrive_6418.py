import time, secrets

class JarvisAutoDrive:
    def __init__(self):
        self.diagnostic_id = f"NAD-{secrets.token_hex(2).upper()}"
        self.vehicle_db = {
            "Hero HF Deluxe": {"mileage": "65-70 kmpl", "tire": "2.75-18"},
            "Pulsar N160": {"mileage": "45-50 kmpl", "tire": "100/80-17"}
        }

    def analyze_vehicle(self, model):
        print(f"\n\033[1;37m--- NEURAL-AUTO-DRIVE ONLINE (ID: {self.diagnostic_id}) ---\033[0m")
        if model in self.vehicle_db:
            specs = self.vehicle_db[model]
            print(f"\033[1;36m[SCANNING] Accessing Blueprints for {model}...\033[0m")
            time.sleep(1)
            print(f"\033[1;32m[REPORT] Optimal Mileage: {specs['mileage']}\033[0m")
            print(f"\033[1;32m[REPORT] Tire Specs: {specs['tire']}\033[0m")
            self.maintenance_advice(model)
        else:
            print("\033[1;31m[ERROR] Vehicle not in current local database.\033[0m")

    def maintenance_advice(self, model):
        print("\033[1;33m[ADVICE] Check oil viscosity and tire pressure for peak performance.\033[0m")
        print(f"\033[1;35m[VOICE] Deepak, for the {model}, I recommend a filter check every 3000km.\033[0m")

if __name__ == "__main__":
    nad = JarvisAutoDrive()
    nad.analyze_vehicle("Pulsar N160")
