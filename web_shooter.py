import time

class WebShooterSystem:
    def __init__(self):
        # Adding Phase Information inside the code
        self.current_phase = 1841
        self.fluid_level = 100  # Percentage
        self.pressure_psi = 300
        print(f"--- Optimus Jarvis Super-Frame | Phase: {self.current_phase} ---")

    def deploy_web(self, mode="Standard"):
        if self.fluid_level > 5:
            print(f"Mode Selected: {mode}")
            print("Calculating trajectory and air resistance...")
            time.sleep(1)
            self.fluid_level -= 5
            print(f"Web Deployed! Remaining Fluid: {self.fluid_level}%")
        else:
            print("Warning: Web fluid critically low. Please refill.")

    def get_phase_status(self):
        return f"This module is part of Phase {self.current_phase}."

if __name__ == "__main__":
    web_sys = WebShooterSystem()
    print(web_sys.get_phase_status())
    web_sys.deploy_web("Impact Web")
