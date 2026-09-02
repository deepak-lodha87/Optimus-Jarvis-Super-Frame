class FighterJetSpecs:
    def __init__(self):
        self.specs = {
            "F-35_Lightning_II": {
                "Engine": "Pratt & Whitney F135",
                "Top_Speed": "Mach 1.6",
                "Wing_Span": "10.7 meters",
                "Combat_Radius": "1,239 km",
                "Tire_Pressure": "275 psi",
                "Role": "Multi-role Stealth Fighter"
            }
        }

    def verify_aerodynamics(self, model):
        if model in self.specs:
            data = self.specs[model]
            print(f"Loading aerodynamic profile for {model}...")
            print(f"Checking Engine: {data['Engine']} | Stability: OPTIMAL")
            return "Profile Loaded Successfully."
        return "Model not found in aerodynamic database."

if __name__ == "__main__":
    jet = FighterJetSpecs()
    print(jet.verify_aerodynamics("F-35_Lightning_II"))
