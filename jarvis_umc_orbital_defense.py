import time
import random

class UniversalMachineController:
    def __init__(self):
        self.shield_density = "GAS"
        self.telepathy_sync = 0 # %
        self.particle_beam_active = False

    def p3528_orbital_deflect(self, incoming_threat):
        if incoming_threat == "LASER":
            return "\033[1;33m[DEFENSE] Orbital Laser detected. Adjusting Hull Mirror-Reflectivity to 99.9%.\033[0m"
        return "[STATUS] Sky perimeter clear of orbital threats."

    def p3529_particle_cannon(self):
        self.particle_beam_active = True
        return "\033[1;31m[TOOLS] Sub-Atomic Beam Online. Material Molecular Dissolution in progress.\033[0m"

    def p3530_neural_telepathy(self, pilot_focus):
        self.telepathy_sync = pilot_focus
        if pilot_focus > 85:
            return "\033[1;35m[COMMS] Neural Telepathy Active. Peer-to-peer data transfer via brainwave sync.\033[0m"
        return "[STATUS] Stabilizing neural link for telepathic bridge."

    def p3531_plasma_solidify(self):
        self.shield_density = "SOLID_STATE"
        return "\033[1;34m[SHIELD] Plasma field compressed to solid state. Physical impact resistance: MAX.\033[0m"

    def p3532_gravity_comms(self):
        return "\033[1;32m[SIGNAL] Sending data via Gravity Waves. Transmission unblockable and infinite range.\033[0m"

if __name__ == "__main__":
    umc = UniversalMachineController()
    print("-" * 60)
    print("   JARVIS UMC: ORBITAL DEFENSE & TELEPATHY (P3528-3532)")
    print("-" * 60)
    
    print(umc.p3528_orbital_deflect("LASER"))
    print(umc.p3529_particle_cannon())
    print(umc.p3530_neural_telepathy(92))
    print(umc.p3531_plasma_solidify())
    print(umc.p3532_gravity_comms())
    
    print("-" * 60)
    print("STATUS: Strategic Defense & Gravity Comms Operational.")
    print("-" * 60)
