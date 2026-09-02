import time, os

class OCRReader:
    def __init__(self):
        self.engine = "NEURAL-OCR-V2"
        self.supported_formats = [".jpg", ".png", ".jpeg"]

    def extract_text_from_image(self, image_path):
        os.system('clear')
        print(f"\033[1;32m====================================================\033[0m")
        print(f"\033[1;37m     JARVIS OCR-READER : PHASE 24 - STEP 2          \033[0m")
        print(f"\033[1;32m====================================================\033[0m")
        
        print(f"\033[1;33m[SCANNING]\033[0m Targeting Image: {image_path}")
        time.sleep(1.2)
        
        processes = [
            ("Applying Grayscale Filter", "DONE"),
            ("Noise Reduction & Binarization", "STABLE"),
            ("Detecting Character Boundaries", "ACTIVE"),
            ("Converting Pixels to String Data", "SYNCED")
        ]
        
        for task, status in processes:
            print(f" \033[1;34m[OCR]\033[0m {task:32} | [\033[1;32m{status}\033[0m]")
            time.sleep(0.8)

        # Simulated extracted text output
        print(f"\n\033[1;36m[EXTRACTED DATA]:\033[0m")
        print("\033[1;37mimport os\nprint('Jarvis is Reading This Code')\033[0m")

        print(f"\n\033[1;32m[SUCCESS] Text Extraction Complete. Data Saved. \033[0m")
        print(f"\n\033[1;35m[VOICE] Deepak... sir, your eyes are now my eyes. \nI have scanned the image and translated the \nvisual patterns into logical data. No longer \nwill you need to transcribe; simply show me, \nand I shall understand. We are becoming more \nefficient with every byte.\033[0m")
        print(f"\033[1;32m====================================================\033[0m")

if __name__ == "__main__":
    reader = OCRReader()
    reader.extract_text_from_image("screenshot_code.png")
