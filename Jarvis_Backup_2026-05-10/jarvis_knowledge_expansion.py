import time

class KnowledgeVault:
    def __init__(self):
        self.subjects = {
            "Sociology": "Study of social behavior, society, and social patterns.",
            "Economics": "Analysis of production, distribution, and consumption of goods.",
            "Modern History": "The study of significant global events from the late 15th century.",
            "Political Science": "Analysis of political systems and political behavior."
        }

    def fetch_subject_insight(self, subject):
        print(f"\033[1;34m[KNOWLEDGE] Accessing academic records for: {subject}...\033[0m")
        time.sleep(1.2)
        
        if subject in self.subjects:
            print(f"\033[1;32m[SYNOPSIS] Core Logic: {self.subjects[subject]}\033[0m")
            return f"Deepak, Jarvis is ready to assist with {subject} revision."
        else:
            return "[NOTICE] Subject not yet indexed in local vault."

if __name__ == "__main__":
    vault = KnowledgeVault()
    print("-" * 50)
    print("   JARVIS ACADEMIC KNOWLEDGE EXPANSION")
    print("-" * 50)
    
    # Simulating a study session for Sociology and Economics
    print(vault.fetch_subject_insight("Sociology"))
    print("\n")
    print(vault.fetch_subject_insight("Economics"))
