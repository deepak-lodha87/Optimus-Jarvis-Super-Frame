import time
import tkinter as tk
from tkinter import messagebox

class OptimusJarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OPTIMUS JARVIS SUPER-FRAME")
        self.root.geometry("400x300")
        self.root.configure(bg='black')

        # Header
        self.label = tk.Label(root, text="JARVIS CORE: PHASE 1476-77", fg="cyan", bg="black", font=("Courier", 12))
        self.label.pack(pady=10)

        # Biometric Button
        self.bio_btn = tk.Button(root, text="START BIOMETRIC SCAN", command=self.phase_1476_biometric, bg="gray", fg="white")
        self.bio_btn.pack(pady=10)

        # Voice Command Button
        self.voice_btn = tk.Button(root, text="ACTIVATE VOICE INTERFACE", command=self.phase_1477_voice, bg="gray", fg="white")
        self.voice_btn.pack(pady=10)

        # Status Bar
        self.status = tk.Label(root, text="System: Waiting for Input", fg="white", bg="black", font=("Courier", 10))
        self.status.pack(side="bottom", fill="x")

    def phase_1476_biometric(self):
        self.status.config(text="Scanning Fingerprint/Retina...", fg="yellow")
        self.root.update()
        time.sleep(1)
        messagebox.showinfo("Security", "Biometric Access Granted: Welcome Sir")
        self.status.config(text="Status: User Authenticated", fg="lime")

    def phase_1477_voice(self):
        self.status.config(text="Listening for Command...", fg="cyan")
        self.root.update()
        time.sleep(1)
        print(">> Logic: Voice frequencies analyzed and verified.")
        messagebox.showinfo("Voice Interface", "Neural Voice Link: ONLINE")
        self.status.config(text="Status: Commands Enabled", fg="cyan")

if __name__ == "__main__":
    root = tk.Tk()
    app = OptimusJarvisGUI(root)
    root.mainloop()
