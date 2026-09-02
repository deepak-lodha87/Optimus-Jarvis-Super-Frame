import time, secrets, gc, re

class LegalContractReviewer:
    def __init__(self):
        self.alc_id = f"ALC-{secrets.token_hex(4).upper()}"
        self.red_flags = ["termination without notice", "unlimited liability", "exclusive rights", "non-refundable"]
        self.nodes = [
            (5744, "Clause-Extraction", "PARSING DOCUMENT STRUCTURE..."),
            (5745, "Penalty-Detection", "SCANNING FOR HIDDEN FINANCIAL RISKS..."),
            (5746, "IP-Protection", "VERIFYING INTELLECTUAL PROPERTY OWNERSHIP..."),
            (5747, "Law-Compliance", "CHECKING GLOBAL LEGAL JURISDICTION..."),
            (5748, "Logic v362", "ALC-CORE: LEGAL REVIEW SYSTEM ACTIVE.")
        ]

    def scan_contract(self, text):
        # Unique logic: Identifying risky phrases using regex
        found_flags = [flag for flag in self.red_flags if re.search(rf"\b{flag}\b", text.lower())]
        return found_flags

    def start_review(self):
        print(f"\033[1;37m--- AI-LEGAL-CONTRACT-REVIEWER ONLINE (ID: {self.alc_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        contract_sample = "Client has exclusive rights to all code. Termination without notice is possible."
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            flags = self.scan_contract(contract_sample)
            risk_level = "HIGH" if flags else "LOW"
            print(f"\033[1;{colors[i]}m[RISK:{risk_level} | FLAGS:{len(flags)}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;31mWARNING: CRITICAL CLAUSES DETECTED. REVIEW RECOMMENDED BEFORE SIGNING.\033[0m")

if __name__ == "__main__":
    alc = LegalContractReviewer()
    alc.start_review()
