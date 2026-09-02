import time
from integrated_core import OptimusIntegratedSystem
from adaptive_core import AdaptiveJarvis
from resource_mgr import ResourceOptimizer

class JarvisMasterController:
    def __init__(self):
        self.sync_engine = OptimusIntegratedSystem()
        self.adaptive_logic = AdaptiveJarvis()
        self.resource_mgr = ResourceOptimizer()

    def initiate_system_check(self):
        print("--- Optimus Jarvis: Full System Boot ---")
        # Resource Check
        self.resource_mgr.monitor_resources()
        # Process and Secure
        status = self.sync_engine.process_and_secure("Cam_Input", "Radar_Data")
        print(status)
        # Self-Correction Run
        final_report = self.adaptive_logic.execute_with_correction("Master Synchronization")
        print(f"Final Status: {final_report}")

if __name__ == "__main__":
    controller = JarvisMasterController()
    controller.initiate_system_check()
