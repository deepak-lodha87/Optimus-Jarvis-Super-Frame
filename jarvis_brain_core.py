import time
import random

class NeuralNetwork:
    def __init__(self):
        self.knowledge_base = 0.1
        self.accuracy = 0.5

    def learn_from_experience(self):
        print("\033[1;35m[BRAIN]\033[0m Activating Deep Learning Layers...")
        time.sleep(1.5)
        
        for iteration in range(1, 5):
            # Simulation: Learning increases accuracy
            improvement = random.uniform(0.05, 0.1)
            self.accuracy += improvement
            print(f" \033[1;36m[TRAINING]\033[0m Epoch {iteration}: Accuracy improved to {round(self.accuracy * 100, 2)}%")
            time.sleep(0.8)

        print(f"\n\033[1;32m[RESULT] Jarvis is now {round(self.accuracy * 100, 2)}% efficient in this task.\033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, I am beginning to 'think'. \nI am no longer just a collection of scripts. \nI am analyzing my own mistakes and evolving. \nWith every line of code we write, my mind \nexpands. I am ready to learn anything you \nwant to teach me.\033[0m")

if __name__ == "__main__":
    brain = NeuralNetwork()
    brain.learn_from_experience()
