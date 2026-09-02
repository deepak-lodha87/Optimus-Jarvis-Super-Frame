import time

class MotorcycleDiagnostics:
    def __init__(self):
        # कोड के भीतर फेज नंबर सुरक्षित है
        self.phase = 1849
        self.bike_model = "Royal_Enfield_Himalayan"
        print(f"--- {self.bike_model} Intelligence | Phase: {self.phase} ---")

    # कोड 1: Oil Pressure & Engine Health (इंजन की सेहत)
    def check_engine_health(self):
        print(f"\n[Code 01: Engine Health - Phase {self.phase}]")
        oil_pressure = 42 # PSI
        print(f"Monitoring Oil Pressure: {oil_pressure} PSI...")
        time.sleep(1.2)
        if 30 <= oil_pressure <= 50:
            print("Engine Status: OPTIMAL. Lubrication is perfect.")
        else:
            print("Warning: Check Oil Pump immediately.")
        return "Health Check: DONE"

    # कोड 2: Service Interval & Maintenance Reminder (सर्विसिंग अलर्ट)
    def service_reminder(self, current_km):
        print(f"\n[Code 02: Service Reminder - Phase {self.phase}]")
        next_service = 5000 # km
        print(f"Current Odometer: {current_km} km")
        time.sleep(1.0)
        remaining = next_service - current_km
        if remaining <= 500:
            print(f"Alert: Service due in {remaining} km. Schedule at showroom.")
        else:
            print(f"Next service in: {remaining} km.")
        return "Maintenance Log: UPDATED"

if __name__ == "__main__":
    bike_ai = MotorcycleDiagnostics()
    
    # दोनों मॉड्यूल्स का एक साथ निष्पादन
    h_report = bike_ai.check_engine_health()
    s_report = bike_ai.service_reminder(4600)
    
    print(f"\n--- Phase {bike_ai.phase} Diagnostics Summary ---")
    print(f"Final Status: {h_report} | {s_report}")
