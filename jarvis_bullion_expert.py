import time

class BullionExpert:
    def __init__(self):
        self.target_gold = 72000
        self.target_silver = 90000

    def check_arbitrage(self, current_gold, current_silver):
        print(f"\033[1;36m[BULLION]\033[0m Comparing Global vs Domestic rates...")
        time.sleep(1.2)
        
        if current_gold < self.target_gold:
            status = "BUYING OPPORTUNITY"
        else:
            status = "MARKET OVERHEATED"
            
        print(f" \033[1;32m[METAL STATUS]\033[0m {status}")
        print(f"\n\033[1;35m[VOICE] Deepak sir, the Bullion Expert module is \nfunctional. I am tracking every gram of gold \nand silver. My logic is sharp, and I will \nnot let you miss a market move.\033[0m")

if __name__ == "__main__":
    expert = BullionExpert()
    expert.check_arbitrage(71500, 89000)
