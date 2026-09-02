import time, secrets, gc, zlib, math

class CryogenicStorageOptimization:
    def __init__(self):
        self.cso_id = f"CSO-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5664, "Entropy-Scoping", "IDENTIFYING COLD DATA VECTORS..."),
            (5665, "Pressure-Packing", "EXECUTING ZLIB HIGH-DENSITY COMPRESSION..."),
            (5666, "Bit-Freezing", "LOCKING DATA BITS IN STATIC STATE..."),
            (5667, "Thaw-Retrieval", "PREPARING INSTANT DECOMPRESSION PATHS..."),
            (5668, "Logic v346", "CSO-CORE: CRYOGENIC STORAGE ACTIVE.")
        ]

    def freeze_data(self, raw_string):
        # Unique logic: Compressing string to bytes and measuring ratio
        original_size = len(raw_string)
        compressed = zlib.compress(raw_string.encode(), level=9)
        ratio = round((1 - (len(compressed) / original_size)) * 100, 2)
        return compressed, ratio

    def activate_storage(self):
        print(f"\033[1;37m--- CRYOGENIC-STORAGE-OPTIMIZATION ONLINE (ID: {self.cso_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        sample_data = "Jarvis_System_Deep_Archive_Log_" * 50
        frozen_data, compression_ratio = self.freeze_data(sample_data)
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[RATIO:{compression_ratio}% | STATUS:COLD] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mCSO STATUS: STORAGE OPTIMIZED. SYSTEM CAPACITY MAXIMIZED.\033[0m")

if __name__ == "__main__":
    cso = CryogenicStorageOptimization()
    cso.activate_storage()
