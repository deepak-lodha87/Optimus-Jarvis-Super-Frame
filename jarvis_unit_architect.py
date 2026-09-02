import os

class UnitArchitect:
    def __init__(self):
        self.master = "Deepak"

    def convert_power(self, hp):
        # Horsepower to Kilowatts (Engineering Standard)
        kw = hp * 0.7457
        return round(kw, 2)

    def convert_fuel(self, gallons):
        # Gallons to Liters (Aviation Standard)
        liters = gallons * 3.78541
        return round(liters, 2)

    def run_demo(self):
        print(f"\n\033[1;33m[UNIT ARCHITECT ACTIVE]\033[0m Processing engineering data...")
        
        hp_value = 500
        kw_result = self.convert_power(hp_value)
        
        msg = f"Deepak sir, 500 Horsepower is equivalent to {kw_result} Kilowatts. Mathematical precision secured."
        
        print(f"\033[1;36m[HP]:\033[0m {hp_value} -> \033[1;32m[KW]:\033[0m {kw_result}")
        os.system(f'termux-tts-speak "{msg}"')

if __name__ == "__main__":
    architect = UnitArchitect()
    architect.run_demo()
