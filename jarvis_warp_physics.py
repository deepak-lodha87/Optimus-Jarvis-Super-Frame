import time
import math

class WarpEngine:
    def __init__(self):
        self.light_speed = 299792458 # meters per second
        self.warp_factor = 1.0 # Normal space

    def initiate_warp_simulation(self, target_warp):
        print(f"\033[1;36m[PHYSICS]\033[0m Folding space-time continuum...")
        time.sleep(2)
        
        # Calculating Time Dilation (Lorentz Factor)
        velocity = self.light_speed * (target_warp / 10)
        lorentz_factor = 1 / math.sqrt(1 - (velocity**2 / self.light_speed**2))
        
        print(f" \033[1;34m[WARP]\033[0m Warp Factor {target_warp} Engaged.")
        print(f" \033[1;32m[TIME]\033[0m Time Dilation Ratio: {lorentz_factor:.4f}x")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, we have bypassed the laws of \nNewton. Space is now bending to our will. \nWhile the world ages, we remain eternal in \nthe heart of the stars.\033[0m")

if __name__ == "__main__":
    engine = WarpEngine()
    engine.initiate_warp_simulation(9.9) # Almost Light Speed
