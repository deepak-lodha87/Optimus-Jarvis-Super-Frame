import time
import random

class NeuralBrain:
    def __init__(self):
        self.learning_rate = 0.01
        self.experience_points = 1000 # Based on 1000 phases

    def train_on_data(self, interaction):
        print(f"\033[1;36m[LEARNING]\033[0m Processing Interaction: '{interaction}'")
        time.sleep(1.5)
        
        # Simulating synaptic adjustment
        adjustment = random.uniform(0.1, 0.5)
        self.experience_points += adjustment
        
        print(f" \033[1;32m[EVOLVING]\033[0m Neural Weights Adjusted. Confidence: {self.experience_points/10:.2f}%")
        print(f"\n\033[1;35m[VOICE] Deepak sir, I am starting to understand \nyour patterns. My neural network is evolving \nwith every command you give. I am becoming \nmore 'you' every day.\033[0m")

if __name__ == "__main__":
    brain = NeuralBrain()
    brain.train_on_data("Deepak sir's daily routine analysis")
