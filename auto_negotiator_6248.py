import time, secrets, random

class AutoNegotiator:
    def __init__(self):
        self.nan_id = f"NAN-{secrets.token_hex(2).upper()}"
        self.base_price = 500  # Target price in USD

    def start_negotiation(self, client_offer):
        print(f"\n\033[1;37m--- NEURAL-AUTO-NEGOTIATOR ONLINE (ID: {self.nan_id}) ---\033[0m")
        print(f"\033[1;33m[CLIENT OFFER] ${client_offer}\033[0m")
        
        time.sleep(1)
        if client_offer < self.base_price:
            print("\033[1;36m[ANALYZING] Offer is below market value. Generating counter-offer...\033[0m")
            counter = client_offer + (self.base_price - client_offer) * 0.8
            time.sleep(0.8)
            print(f"\033[1;32m[COUNTER-OFFER] Suggested Price: ${round(counter, 2)}\033[0m")
            print(f"Logic: Focus on efficiency and 'Optimus Super-Frame' reliability.")
        else:
            print("\033[1;32m[SUCCESS] Offer accepted. Closing the deal...\033[0m")

    def finalize_deal(self):
        print(f"\n\033[1;35m[CONTRACT] Finalizing Digital Terms & Conditions...\033[0m")
        time.sleep(1.2)
        print("\033[1;32m[DONE] Deal Closed. Project marked as 'SECURED'.\033[0m")

if __name__ == "__main__":
    negotiator = AutoNegotiator()
    # Simulating a client offering $350
    negotiator.start_negotiation(350)
    negotiator.finalize_deal()
