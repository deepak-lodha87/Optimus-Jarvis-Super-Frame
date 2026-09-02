import time, secrets, gc

class SubscriptionCanceller:
    def __init__(self):
        self.asc_id = f"ASC-{secrets.token_hex(4).upper()}"
        self.transactions = [
            {"name": "Python IDE Pro", "amount": 15, "usage_hr": 40},
            {"name": "Music Streamer", "amount": 10, "usage_hr": 2},
            {"name": "Old Cloud Storage", "amount": 5, "usage_hr": 0}
        ]
        self.nodes = [
            (5764, "Recur-Scrape", "IDENTIFYING RECURRING PAYMENTS..."),
            (5765, "Usage-Track", "ANALYZING TOOL UTILIZATION DATA..."),
            (5766, "Auto-Cancel", "FLAGGING LOW-VALUE SERVICES..."),
            (5767, "Free-Alt-Finder", "LOCATING OPEN-SOURCE ALTERNATIVES..."),
            (5768, "Logic v366", "ASC-CORE: COST REDUCTION ACTIVE.")
        ]

    def find_waste(self):
        # Unique logic: Flagging subs where usage is less than 5 hours/month
        return list(filter(lambda x: x['usage_hr'] < 5, self.transactions))

    def run_canceller_audit(self):
        print(f"\033[1;37m--- AUTOMATED-SUBSCRIPTION-CANCELLER ONLINE (ID: {self.asc_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        waste = self.find_waste()
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            waste_count = len(waste)
            print(f"\033[1;{colors[i]}m[WASTE_FOUND:{waste_count} | SAVING:ACTIVE] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print(f"\033[1;32mASC STATUS: AUDIT COMPLETE. CANCEL RECOMMENDATIONS SENT FOR {len(waste)} SERVICES.\033[0m")

if __name__ == "__main__":
    asc = SubscriptionCanceller()
    asc.run_canceller_audit()
