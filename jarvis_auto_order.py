import os
import time

class LogisticsManager:
    def __init__(self):
        self.master = "Deepak"

    def source_parts(self, component_name):
        print(f"\n\033[1;33m[SUPPLY CHAIN]\033[0m Sourcing {component_name} from global databases...")
        time.sleep(1.5)
        
        # सिमुलेटेड डेटा: हकीकत में यहाँ API काम करेगा
        results = [
            {"Source": "Authorized Dealer", "Price": "₹1,200", "Delivery": "2 Days"},
            {"Source": "Aftermarket Hub", "Price": "₹850", "Delivery": "4 Days"}
        ]
        
        for res in results:
            print(f"\033[1;32m[FOUND]\033[0m {res['Source']} | Price: {res['Price']} | ETA: {res['Delivery']}")
            time.sleep(0.5)

    def ask_permission(self, component):
        msg = f"Deepak sir, I have found the {component} online. Should I add it to the cart or wait for your manual inspection?"
        os.system(f'termux-tts-speak "{msg}"')
        print(f"\n\033[1;35m[AWAITING COMMAND]:\033[0m Type 'Order' to proceed.")

if __name__ == "__main__":
    logistics = LogisticsManager()
    # उदाहरण: पिछले फेज में फेल होने वाला 'Alternator Belt'
    logistics.source_parts("Alternator Belt")
    logistics.ask_permission("Alternator Belt")
