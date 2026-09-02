import time, random

def deploy_advanced_tech(phase_name, sub_techs):
    print(f"\n\033[1;35m[SYSTEM]: Initializing {phase_name}...\033[0m")
    for tech in sub_techs:
        time.sleep(0.4)
        print(f">> {tech}... \033[1;32mONLINE\033[0m")

if __name__ == "__main__":
    print("="*60 + "\n          OPTIMUS JARVIS SUPER-FRAME: ELITE MODULES          \n" + "="*60)
    
    # Phase 2115: Magnetic Manipulation (Magneto Style)
    deploy_advanced_tech("PHASE 2115: MAGNETIC MANIPULATION", [
        "Ferromagnetic_Field_Generator", 
        "Polarity_Inversion_Core", 
        "Metal_Structural_Levitation"
    ])
    
    print("-" * 40)
    
    # Phase 2116: Cybernetic Hacking Link (Digital Warfare)
    deploy_advanced_tech("PHASE 2116: CYBERNETIC HACKING LINK", [
        "Brute_Force_Bypass_v4", 
        "Encryption_Key_Decipher", 
        "Remote_Satellite_Override"
    ])
    
    hacker_status = random.randint(99, 100)
    print(f"\n\033[1;31m[JARVIS]: Hacking penetration capability at {hacker_status}%. All firewalls are vulnerable.\033[0m")
    print("="*60)
