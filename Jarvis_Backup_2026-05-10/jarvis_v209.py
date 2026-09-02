import os
import time

def password_vault_protocol():
    print("\n" + "="*40)
    print("      JARVIS SECURE PASSWORD VAULT")
    print("="*40)
    
    action = input("\n[JARVIS]: Would you like to (A)dd a password or (R)etrieve one? ").lower()
    
    if action == 'a':
        site = input("[INPUT]: Enter Account/Website name: ")
        pwd = input("[INPUT]: Enter Password: ")
        
        with open("vault_data.txt", "a") as vault:
            vault.write(f"Account: {site} | Password: {pwd}\n")
        
        msg = "Data secured in the vault, Commander."
        print(f"\n[JARVIS]: {msg}")
        os.system(f"termux-tts-speak '{msg}'")
        
    elif action == 'r':
        print("\n" + "-"*30)
        print("      VAULT RECORDS")
        print("-"*30)
        if os.path.exists("vault_data.txt"):
            with open("vault_data.txt", "r") as vault:
                print(vault.read())
        else:
            print("[EMPTY]: Vault is currently empty.")
        print("-"*30)
    else:
        print("[ERROR]: Invalid selection.")

if __name__ == "__main__":
    password_vault_protocol()
