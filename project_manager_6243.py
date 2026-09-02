import time, secrets

class ProjectManager:
    def __init__(self):
        self.npm_id = f"NPM-{secrets.token_hex(2).upper()}"
        self.projects = [
            {"name": "Web Scraper", "status": "Active", "deadline": "2 Days", "prio": "High"},
            {"name": "API Auth", "status": "Pending", "deadline": "5 Days", "prio": "Medium"},
            {"name": "Data Analysis", "status": "Review", "deadline": "1 Day", "prio": "Critical"}
        ]

    def display_dashboard(self):
        print(f"\n\033[1;37m--- JARVIS PROJECT DASHBOARD (ID: {self.npm_id}) ---\033[0m")
        print(f"{'Project Name':<18} | {'Status':<10} | {'Deadline':<10} | {'Priority'}")
        print("-" * 60)
        
        for p in self.projects:
            color = "\033[1;32m" if p['prio'] == "High" else "\033[1;33m"
            if p['prio'] == "Critical": color = "\033[1;31m"
            
            print(f"{p['name']:<18} | {p['status']:<10} | {p['deadline']:<10} | {color}{p['prio']}\033[0m")
            time.sleep(0.2)

    def generate_invoice(self, project_name):
        print(f"\n\033[1;36m[BILLING] Generating Invoice for {project_name}...\033[0m")
        time.sleep(1)
        invoice_no = secrets.token_hex(4).upper()
        print(f"\033[1;32m[SUCCESS] Invoice #{invoice_no} created. Status: Sent to Client.\033[0m")

if __name__ == "__main__":
    npm = ProjectManager()
    npm.display_dashboard()
    npm.generate_invoice("Data Analysis")
