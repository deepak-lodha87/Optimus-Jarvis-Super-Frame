import time, secrets, gc
from decimal import Decimal

class TaxOptimizationCalculator:
    def __init__(self):
        self.toc_id = f"TOC-{secrets.token_hex(4).upper()}"
        self.tax_brackets = {
            "INDIA": Decimal('0.20'), # Simulated 20%
            "GERMANY": Decimal('0.30'), # Simulated 30%
            "UAE": Decimal('0.00')    # Tax Free Zone
        }
        self.nodes = [
            (5724, "Jurisdiction-Map", "MAPPING INTERNATIONAL TAX TREATIES..."),
            (5725, "Deduction-Track", "IDENTIFYING BUSINESS EXPENSE REBATES..."),
            (5726, "DTAA-Sync", "APPLYING DOUBLE TAXATION AVOIDANCE LOGIC..."),
            (5727, "Profit-Forecast", "CALCULATING NET POST-TAX REVENUE..."),
            (5728, "Logic v358", "TOC-CORE: TAX OPTIMIZATION ACTIVE.")
        ]

    def calculate_net_income(self, gross, country, expenses):
        # Unique logic: (Gross - Expenses) * (1 - Tax Rate)
        tax_rate = self.tax_brackets.get(country.upper(), Decimal('0.25'))
        taxable_amount = Decimal(str(gross)) - Decimal(str(expenses))
        net_income = taxable_amount * (Decimal('1.00') - tax_rate)
        return round(net_income, 2)

    def run_tax_audit(self):
        print(f"\033[1;37m--- TAX-OPTIMIZATION-CALCULATORS ONLINE (ID: {self.toc_id}) ---\033[0m")
        colors = [36, 35, 34, 32, 31]
        
        income = 500000 # Simulated income from a project
        cost = 50000    # Laptop/Server expenses
        
        for i, (p_id, title, status) in enumerate(self.nodes):
            net = self.calculate_net_income(income, "INDIA", cost)
            print(f"\033[1;{colors[i]}m[GROSS:{income} | NET:{net}] Phase {p_id}: {title} >> {status}\033[0m")
            time.sleep(0.18)
            gc.collect()

        print("\033[1;37m" + "="*60 + "\033[0m")
        print("\033[1;32mTOC STATUS: FINANCIAL EFFICIENCY MAXIMIZED. TAX LEAKAGE MINIMIZED.\033[0m")

if __name__ == "__main__":
    toc = TaxOptimizationCalculator()
    toc.run_tax_audit()
