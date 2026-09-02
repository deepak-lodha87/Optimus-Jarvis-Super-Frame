import time

class FuelDynamics:
    def __init__(self, vehicle_name):
        self.vehicle = vehicle_name
        self.status = "Analyzing"

    def calculate_range(self, fuel_liters, avg_mileage):
        """Fuel aur mileage ke base par range nikalna."""
        estimated_range = fuel_liters * avg_mileage
        print(f"\033[1;36m[ANALYSIS] Calculating potential range for {self.vehicle}...\033[0m")
        time.sleep(1)
        return estimated_range

    def efficiency_report(self, distance, fuel_consumed):
        """Current trip ki efficiency check karna."""
        efficiency = distance / fuel_consumed
        if efficiency < 15:
            return f"\033[1;31m[ALERT] Low Efficiency ({efficiency} km/l). Check Air Filter/Tire Pressure.\033[0m"
        else:
            return f"\033[1;32m[OPTIMAL] Good Efficiency ({efficiency} km/l). Engine performing well.\033[0m"

if __name__ == "__main__":
    # Example: Testing with your Hero HF Deluxe (Approx 9.5L Tank, 65km/l mileage)
    hf_deluxe = FuelDynamics("Hero HF Deluxe")
    print("-" * 45)
    print("   JARVIS FUEL & RANGE ANALYZER")
    print("-" * 45)
    
    range_left = hf_deluxe.calculate_range(5, 65) # 5 liters left
    print(f">> Estimated Range Left: {range_left} KM")
    
    # Testing Efficiency
    report = hf_deluxe.efficiency_report(100, 2) # 100km in 2 liters
    print(report)
