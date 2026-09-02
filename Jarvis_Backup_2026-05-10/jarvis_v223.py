import os
import time

def expenditure_tracker_protocol():
    print("\n" + "="*40)
    print("      JARVIS EXPENDITURE TRACKER")
    print("="*40)
    
    msg_ask = "Commander Deepak, please enter the item name and the amount spent."
    print(f"\n[JARVIS]: {msg_ask}")
    os.system(f"termux-tts-speak '{msg_ask}'")
    
    item = input("\n[INPUT]: Item/Description: ")
    try:
        amount = float(input("[INPUT]: Amount (e.g., 50.50): "))
        
        # डेटा को एक्सपेंस फाइल में सेव करना
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        expense_entry = f"[{timestamp}] ITEM: {item} | AMOUNT: {amount}\n"
        
        with open("expense_log.txt", "a") as f:
            f.write(expense_entry)
            
        success = f"Transaction for {item} has been logged in the financial core."
        print(f"\n[JARVIS]: {success}")
        os.system(f"termux-tts-speak '{success}'")
        
    except ValueError:
        error = "Commander, please provide a numeric value for the amount."
        print(f"\n[ERROR]: {error}")
        os.system(f"termux-tts-speak '{error}'")

    # कुल खर्च देखने का विकल्प
    view = input("\n[JARVIS]: View recent transactions? (y/n): ").lower()
    if view == 'y':
        if os.path.exists("expense_log.txt"):
            print("\n" + "-"*30)
            with open("expense_log.txt", "r") as f:
                print(f.read())
            print("-"*30)
        else:
            print("

