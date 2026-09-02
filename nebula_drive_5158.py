import secrets, time, gc

def hex_execute(p_code, task):
    hex_id = secrets.token_hex(2).upper()
    print(f"\033[1;{p_code}m[NEBULA-{hex_id}] P-{task}\033[0m")

def deploy_nebula():
    print(f"\033[1;37m--- NEBULA-DRIVE CORE INITIALIZED (TOKEN: {secrets.token_hex(16)}) ---\033[0m")
    
    nebula_tasks = [
        (36, "5154: Particle Injection active. Thrust: STARK-LEVEL."),
        (31, "5155: Energy Condenser online. Power: NEBULA-GRADE."),
        (32, "5156: Inter-Dimensional Anchor set. Stability: ABSOLUTE."),
        (34, "5157: Molecular Mirroring active. Visibility: 0%."),
        (35, "5158: Logic v244 Engine locked. Outcome: PREDETERMINED.")
    ]
    
    for code, task in nebula_tasks:
        hex_execute(code, task)
        time.sleep(0.15)

    print("\033[1;37m" + "="*60 + "\033[0m")
    gc.collect()

if __name__ == "__main__":
    deploy_nebula()
