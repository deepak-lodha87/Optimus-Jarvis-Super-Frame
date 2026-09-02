import time
import random

class EarthForceManagement:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित हैं
        self.phase_volcano = 1966
        self.phase_tsunami = 1967
        print(f"--- Optimus Jarvis Super-Frame ---")
        print(f"Initializing Planetary Protection: {self.phase_volcano} & {self.phase_tsunami}")

    # Phase 1966: Volcanic Energy Extraction (ज्वालामुखी ऊर्जा संचयन)
    def extract_magma_energy(self, volcano_id):
        print(f"\n[Code 01: Volcanic Extraction - Phase {self.phase_volcano}]")
        print(f"Deploying thermal-resistant probes into {volcano_id} magma chamber...")
        time.sleep(2.0)
        
        # ऊष्मा से ऊर्जा का सिमुलेशन
        core_temp = random.randint(800, 1200)
        energy_mw = core_temp * 1.5
        print(f"Magma Temperature: {core_temp}°C | Power Generated: {energy_mw} MW")
        print("Status: Geothermal turbines operating at peak efficiency.")
        return "Energy: VOLCANIC_POWER_CONNECTED"

    # Phase 1967: Tsunami Early Warning System (सुनामी चेतावनी तंत्र)
    def monitor_oceanic_pressure(self):
        print(f"\n[Code 02: Tsunami Detection - Phase {self.phase_tsunami}]")
        print("Analyzing deep-sea pressure sensors (DART buoy network)...")
        time.sleep(1.5)
        
        wave_height_meters = random.uniform(0.1, 15.0)
        print(f"Detected Wave Delta: {wave_height_meters:.2f} meters.")
        
        if wave_height_meters > 5.0:
            print("CRITICAL ALERT: Tsunami signature detected! Calculating landfall time...")
            return "Alert: TSUNAMI_EVACUATION_REQUIRED"
        else:
            print("Status: Sea levels within normal range. Safe for coastal operations.")
            return "Alert: NONE"

if __name__ == "__main__":
    earth_ai = EarthForceManagement()
    
    # दोनों फेजेस का निष्पादन
    v_report = earth_ai.extract_magma_energy("Mount_Vesuvius_Node")
    t_report = earth_ai.monitor_oceanic_pressure()
    
    print(f"\n--- Earth Resources & Safety Summary ---")
    print(f"Final Report: {v_report} | {t_report}")
