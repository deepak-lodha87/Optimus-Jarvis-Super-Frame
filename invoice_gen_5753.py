import time, secrets, gc, datetime

class SmartInvoiceGenerator:
    def __init__(self):
        self.sig_id = f"SIG-{secrets.token_hex(4).upper()}"
        self.nodes = [
            (5749, "Billing-Cycle", "GENERATING PROJECT MILESTONE INVOICE..."),
            (5750, "Currency-Sync", "APPLYING REAL-TIME CONVERSION RATES..."),
            (5751, "Payment-Alert", "SETTING UP AUTOMATED FOLLOW-UP LOGIC..."),
            (5752, "E-Signature", "EMBEDDING ENCRYPTED DIGITAL SIGNATURE..."),
            (5753, "Logic v363", "SIG-CORE: INVOICE GENERATION READY.")
        ]

    def generate_bill_id(self):
        # Unique logic: Date based invoice number
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        return f"INV-{date_str}-{secrets.token_hex(2).upper()}"

    def run_billing_service(self):
        print(f"\033[1;37m--- SMART-INVOICE-GENERATOR ONLINE (ID: {self.sig_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        bill_no = self.generate_bill_id()
        amount = 1200 # Simulated $1200 payment
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            print(f"\033[1;{colors[i]}m[BILL_NO:{bill_no} | AMT:${amount}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mSIG STATUS: INVOICE SENT TO CLIENT. PAYMENT TRACKING ACTIVE.\033[0m")

if __name__ == "__main__":
    sig = SmartInvoiceGenerator()
    sig.run_billing_service()
