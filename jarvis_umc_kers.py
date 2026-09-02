import time

class UniversalMachineController:
    def __init__(self, machine_id):
        self.id = machine_id
        self.flywheel_rpm = 0
        self.boost_ready = False

    def capture_kinetic_energy(self, current_speed):
        """Phase 3229: Diverting waste energy to Flywheel"""
        print(f"\033[1;34m[KERS] Engaging Vacuum-Sealed Flywheel for {self.id}...\033[0m")
        time.sleep(1)
        # Charging the mechanical battery
        self.flywheel_rpm = current_speed * 500
        print(f"  • Flywheel Rotation: {self.flywheel_rpm} RPM [CHARGING]")
        if self.flywheel_rpm > 20000:
            self.boost_ready = True
        return f"\033[1;32m[STATUS] Kinetic Energy Reservoir: {self.flywheel_rpm/400:.1f}%\033[0m"

    def deploy_instant_boost(self):
        """Phase 3230: Releasing stored momentum to the drivetrain"""
        if not self.boost_ready:
            return "\033[1;31m[ERROR] Insufficient Kinetic Charge.\033[0m"
        
        print("\033[1;35m[BOOST] Disengaging Flywheel Clutch... RELEASING TORQUE!\033[0m")
        time.sleep(0.5)
        self.flywheel_rpm = 0
        self.boost_ready = False
        return "\033[1;32m[SUCCESS] 400HP Instant Surge Delivered to Wheels/Propeller.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController("Optimus_Interceptor")
    
    print("-" * 60)
    print("   JARVIS UMC: KINETIC BOOST & FLYWHEEL LOGIC (P3229-30)")
    print("-" * 60)
    
    # Simulating high-speed braking to charge KERS
    print(umc.capture_kinetic_energy(80))
    # Deploying the mechanical boost
    print("\n" + umc.deploy_instant_boost())
    print("-" * 60)
