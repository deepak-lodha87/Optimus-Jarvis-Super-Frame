import json

class EngineIntelligence:
    def __init__(self):
        # Database for high-precision engine specs
        self.engine_specs = {
            "v12_biturbo": {
                "displacement": "6.0L",
                "horsepower": "621 hp",
                "torque": "738 lb-ft",
                "fuel_system": "Direct Injection",
                "cooling": "Liquid Cooled"
            },
            "electric_powertrain": {
                "voltage": "800V",
                "battery_capacity": "100kWh",
                "motor_type": "Permanent Magnet Synchronous",
                "efficiency": "94%"
            }
        }

    def get_specs(self, engine_type):
        engine_type = engine_type.lower()
        if engine_type in self.engine_specs:
            return self.engine_specs[engine_type]
        else:
            return "Engine data not found in current database."

# Initializing P401 Logic
jarvis_engine = EngineIntelligence()
print("P401: Engine Specification Logic - Active")
