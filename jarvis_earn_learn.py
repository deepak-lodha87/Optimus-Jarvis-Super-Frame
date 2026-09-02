import time

def trade_logic(current_balance):
    print("--------------------------------------------------")
    print(f"[JARVIS] Current Wallet: ₹{current_balance}")
    
    # Jarvis pehle seekhega (Analysis)
    print("[SYSTEM] Analyzing Global Markets...")
    time.sleep(2) 
    
    # Phir execute karega (Earning)
    profit_percent = 2.0 # Aaj ka target
    daily_profit = current_balance * (profit_percent / 100)
    new_balance = current_balance + daily_profit
    
    print(f"[SUCCESS] Aaj ka munafa: ₹{daily_profit}")
    print(f"[UPDATE] Naya balance: ₹{new_balance}")
    print("[LEARNING] Aaj ki strategy 'Success' rahi. Memory saved.")
    print("--------------------------------------------------")
    return new_balance

# Simulation shuru karein
# balance = 1000
# balance = trade_logic(balance)
