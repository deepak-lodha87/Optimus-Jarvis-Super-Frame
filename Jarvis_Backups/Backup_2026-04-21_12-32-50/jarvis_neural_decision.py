import time
import random

class NeuralDecisionEngine:
    def __init__(self):
        self.knowledge_base = {
            "High Speed": ["Titanium", "Aerodynamic", "Fighter Jet"],
            "Heavy Load": ["Steel", "Reinforced Chassis", "Truck"],
            "Fuel Efficiency": ["Carbon Fiber", "Low Drag", "Electric Vehicle"]
        }

    def train_and_decide(self, objective):
        print(f"\033[1;34m[NEURAL] Training model for Objective: {objective}...\033[0m")
        time.sleep(1.5)
        
        if objective in self.knowledge_base:
            recommendations = self.knowledge_base[objective]
            print("\033[1;32m[DECISION] Optimized Strategy Found:\033[0m")
            print(f"  • Recommended Material: {recommendations[0]}")
            print(f"  • Structural Focus: {recommendations[1]}")
            print(f"  • Vehicle Type: {recommendations[2]}")
        else:
            print("\033[1;31m[ERROR] Insufficient data to make a neural decision.\033[0m")

if __name__ == "__main__":
    brain = NeuralDecisionEngine()
    print("-" * 50)
    print("   JARVIS NEURAL DECISION MATRIX (Phase 3059)")
    print("-" * 50)
    
    # Jarvis decide karega ki Fuel Efficiency ke liye kya best hai
    brain.train_and_decide("Fuel Efficiency")
    print("\n")
    # Jarvis decide karega ki High Speed ke liye kya best hai
    brain.train_and_decide("High Speed")
