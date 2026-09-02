import time

class OptimusJarvis:
    def __init__(self, name):
        self.name = name
        self.status = "Offline"
        self.system_check = False

    def self_diagnosis(self):
        print(f"[{self.name}] Running Self-Diagnosis...")
        time.sleep(1)
        self.system_check = True 
        print("Diagnosis Complete: No defects detected.")

    def perception_module(self):
        if self.system_check:
            self.status = "Active"
            print("Perception Module: Online. Awaiting input, Deepak Sir.")
        else:
            print("Error: System integrity check failed.")

jarvis = OptimusJarvis("Optimus Jarvis Super-Frame")
jarvis.self_diagnosis()
jarvis.perception_module()
