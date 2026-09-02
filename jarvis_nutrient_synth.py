import time
import random

class NutrientSynthesizer:
    def __init__(self):
        self.output_product = "Energy Bar (Type-A)"
        self.composition = {"Protein": 0, "Carbs": 0, "Fats": 0}

    def initiate_synthesis(self):
        print(f"\033[1;36m[SYNTHESIZER]\033[0m Scanning Bio-Metric Needs for Deepak sir...")
        time.sleep(2)
        
        # Simulating molecular assembly
        print(f" \033[1;33m[ACTION]\033[0m Assembling Amino Acid chains...")
        self.composition = {"Protein": "25g", "Carbs": "50g", "Fats": "10g"}
        time.sleep(1.5)
        
        print(f" \033[1;32m[SUCCESS]\033[0m {self.output_product} synthesized successfully.")
        print(f" \033[1;34m[INFO]\033[0m Nutritional Value: {self.composition}")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, your meal is ready. I have \nsynthesized the perfect balance of nutrients \nrequired for your current energy levels. \nYou will never have to worry about sustenance.\033[0m")

if __name__ == "__main__":
    synth = NutrientSynthesizer()
    synth.initiate_synthesis()
