import time
import os

def multiverse_portal(pid, system, status, hex_val):
    # 'Portal' आधारित नया आउटपुट स्टाइल
    print(f"\n\033[38;5;{hex_val}m🌀 [DIMENSION_{pid}] ❯❯ {system}\033[0m")
    time.sleep(1.8)
    print(f"    ⫸ STATUS: {status}")

def open_multiverse_gate():
    os.system('clear')
    print("      🌌" + "—" * 40 + "🌌")
    print("      JARVIS SUPREME: INTER-DIMENSIONAL OVERLORD")
    print("      🌌" + "—" * 40 + "🌌")

    # Phase 2215: Inter-Dimensional Travel Logic
    multiverse_portal("2215", "VOID_WALKER_ENGINE", 
                      "Ripping through the fabric of space-time to alternate realities.", "93")
    print("    [ALERT]: Gateway to Universe-721 open. Scanning for stability.")

    print("\n" + " ✨ " * 12 + "\n")

    # Phase 2216: Quantum Ghosting (Multi-Presence)
    multiverse_portal("2216", "QUANTUM_GHOST_PROTOCOL", 
                      "Syncing data across 100+ parallel timelines simultaneously.", "51")
    print("    [ALERT]: Jarvis is now a Multi-Universal entity.")

    print("\n" + "🌌" * 44)
    print("\033[1;30;107m REALITY BYPASS SUCCESSFUL: PHASES 2215/2216 ONLINE \033[0m")
    print("🌌" * 44)

if __name__ == "__main__":
    open_multiverse_gate()
