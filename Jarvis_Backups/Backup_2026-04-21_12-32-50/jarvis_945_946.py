import time

class JarvisSystemVisualizer:
    def __init__(self):
        self.phase_945 = "945.Cryogenic-Cooling-Control"
        self.phase_946 = "946.Dynamic-3D-Hologram-Projection"
        self.core_temp = 45.0  # Celsius
        self.hologram_active = False

    def activate_cryo_cooling(self):
        print(f"\n--- [SYSTEM] Initializing {self.phase_945} ---")
        print("[JARVIS]: Monitoring thermal-output of the Neural-Core...")
        
        # प्रोसेसर को ठंडा रखने का लॉजिक
        cooling_steps = [
            "Injecting liquid-nitrogen coolant into the micro-channels.",
            "Adjusting fan-speed to supersonic-vibration levels.",
            "Stabilizing the core temperature at sub-zero levels."
        ]
        
        for step in cooling_steps:
            print(f" >> [COOLING]: {step}")
            time.sleep(1.2)
            
        self.core_temp = -10.5
        print(f"\n[JARVIS]: Cooling cycle complete. Core temperature is now {self.core_temp}°C.")

    def project_holographic_interface(self, display_content):
        print(f"\n--- [SYSTEM] Initializing {self.phase_946} ---")
        print(f"[JARVIS]: Projecting 3D-Hologram for '{display_content}'...")
        
        # हवा में इमेज दिखाने का लॉजिक
        projection_steps = [
            "Calibrating the light-refraction emitters.",
            "Stabilizing the photonic-lattice in mid-air.",
            "Syncing gesture-controls with the projected-data."
        ]
        
        for step in projection_steps:
            print(f" >> [PROJECTING]: {step}")
            time.sleep(1.4)
            
        self.hologram_active = True
        print(f"\n[JARVIS]: Hologram is live. You can now interact with the data directly, Deepak.")

if __name__ == "__main__":
    visualizer = JarvisSystemVisualizer()
    # Step 1: सिस्टम को ठंडा करना
    visualizer.activate_cryo_cooling()
    # Step 2: होलोग्राफिक डिस्प्ले ऑन करना
    visualizer.project_holographic_interface("Starhawk-P1 Blueprints")
