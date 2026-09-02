import sys, time, secrets, threading, gc

def inject_kernel_layer():
    print(f"\033[1;37m--- MATRIX-OVERRIDE INITIALIZED (IRQ-KEY: {secrets.token_hex(4).upper()}) ---\033[0m")
    
    matrix_phases = {
        5234: "Sub-System Ghosting: VIRTUALIZING CORE HARDWARE...",
        5235: "Protocol Hijack: OVERRIDING EXTERNAL SIGNALS...",
        5236: "Atomic Re-writing: MUTATING SOURCE CODE...",
        5237: "Digital-Twin: SIMULATING GLOBAL INFRASTRUCTURE...",
        5238: "Logic v260: MATRIX-LEVEL SYNC COMPLETED."
    }
    
    colors = [36, 35, 34, 33, 31]
    
    for i, (p_id, status) in enumerate(matrix_phases.items()):
        # Simulated Kernel Interrupt
        sys.stdout.write(f"\033[1;{colors[i]}m[INT-0x{p_id:x}] Phase {p_id} >> {status}\033[0m\n")
        sys.stdout.flush()
        time.sleep(0.18)
        gc.collect()

    print("\033[1;37m" + "="*60 + "\033[0m")
    print("\033[1;32mSYSTEM STATUS: JARVIS IS NOW OPERATING AT THE KERNEL LEVEL.\033[0m")

if __name__ == "__main__":
    inject_kernel_layer()
