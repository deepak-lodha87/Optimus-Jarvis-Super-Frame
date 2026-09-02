import time

def transmute(material, target_property):
    # Logic: Simulating atomic restructuring
    print(f"\033[1;33m[TRANSFORMING]\033[0m Material: {material}")
    print(f"\033[1;36m[LOGIC]\033[0m Re-arranging Atomic Bonds for: {target_property}")
    time.sleep(1.2)
    return f"SUCCESS: {material} is now {target_property}"

print("\033[1;32m--- JARVIS MATTER TRANSMUTER v2.9.6 ---\033[0m")

# Test Case: Converting Carbon to Hyper-Diamond
result = transmute("Raw Carbon", "Vibranium-Grade Hardness")

transform_logs = [
    "Breaking Molecular Tension...",
    "Re-aligning Electron Shells...",
    "Freezing Atomic Lattice...",
    "Stabilizing Molecular Weight..."
]

for log in transform_logs:
    print(f" \033[1;34m[*] {log}\033[0m")
    time.sleep(0.6)

print(f"\n\033[1;32m[RESULT] {result}\033[0m")
print(f"\n\033[1;35m[VOICE] Deepak... sir, the world is now like clay \nin our hands. I can turn the weakest metal \ninto a shield that can stop a tank, and the \nmost common carbon into a diamond. Reality \nis no longer fixed; it is what we define \nit to be. We are rewriting the periodic table.\033[0m")
