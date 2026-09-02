class VehicleBlueprint:
    def __init__(self):
        self.database = {
            "Drone_X1": {
                "Type": "UAV",
                "Mileage": "45 mins flight time",
                "Battery": "5000mAh LiPo",
                "Tire_Specs": "N/A (Landing Gear)",
                "Build": "Carbon Fiber Frame"
            },
            "Electric_Bike_01": {
                "Type": "Motorcycle",
                "Range": "150 km per charge",
                "Tire_Specs": "110/70-17 Front, 140/70-17 Rear",
                "Power_Train": "72V Brushless DC Motor",
                "Build": "Trellis Frame"
            }
        }

    def get_specs(self, model):
        print(f"Retrieving blueprint for: {model}...")
        return self.database.get(model, "Model not found in database.")

if __name__ == "__main__":
    db = VehicleBlueprint()
    # Cross-checking specs for precision
    print(db.get_specs("Electric_Bike_01"))
