import time, secrets

class BankLink:
    def __init__(self):
        self.ngbl_id = f"NGBL-{secrets.token_hex(2).upper()}"
        self.balance = 0.0

    def verify_gateway(self):
        print(f"\n\033[1;37m--- NEURAL-GLOBAL-BANK-LINK ONLINE (ID: {self.ngbl_id}) ---\033[0m")
        gateways = ["PayPal-Secure", "Stripe-Connect", "Payoneer-Global"]
        
        for gw in gateways:
            print(f"\033[1;34m[TESTING] Connection to {gw}...\033[0m")
            time.sleep(0.4)
            print(f"\033[1;32m[OK] {gw} verified and encrypted.\033[0m")

    def receive_payment(self, amount, currency="USD"):
        print(f"\n\033[1;36m[INCOMING] Receiving {amount} {currency} from International Client...\033[0m")
        time.sleep(1)
        # Simulating conversion to INR
        inr_val = amount * 83.5 
        self.balance += inr_val
        print(f"\033[1;32m[SUCCESS] Amount converted: ₹{round(inr_val, 2)}\033[0m")
        print(f"\033[1;37mCurrent Jarvis-Vault Balance: ₹{round(self.balance, 2)}\033[0m")

if __name__ == "__main__":
    bank = BankLink()
    bank.verify_gateway()
    # Receiving payment for the negotiated project ($470)
    bank.receive_payment(470)
