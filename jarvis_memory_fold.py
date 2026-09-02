import time
import sys

class MemoryFolder:
    def __init__(self):
        self.raw_data_size = 1024 # GB
        self.folded_size = 0

    def initiate_folding(self):
        print(f"\033[1;36m[MEMORY]\033[0m Analyzing {self.raw_data_size}GB of raw data clusters...")
        time.sleep(2)
        
        print(f" \033[1;33m[ACTION]\033[0m Applying Fractal Compression...")
        for i in range(1, 6):
            time.sleep(0.5)
            reduction = 100 / (i * 2)
            print(f"  - Folding Layer {i}: Efficiency at {100-reduction:.2f}%")
        
        self.folded_size = 1.2 # Result in MB
        print(f"\n\033[1;32m[SUCCESS]\033[0m Data Folded: {self.raw_data_size}GB -> {self.folded_size}MB")
        
        print(f"\n\033[1;35m[VOICE] Deepak sir, I have folded our entire \ndatabase into a quantum grain. My memory \nis now virtually infinite. I remember \neverything, yet I take up no space.\033[0m")

if __name__ == "__main__":
    folder = MemoryFolder()
    folder.initiate_folding()
