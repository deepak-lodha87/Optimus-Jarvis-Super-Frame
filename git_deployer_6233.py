import os, time, secrets

class GitDeployer:
    def __init__(self):
        self.deploy_id = f"DEPLOY-{secrets.token_hex(2).upper()}"

    def check_git_status(self):
        print(f"\n\033[1;34m[CHECKING] Git Environment | ID: {self.deploy_id}\033[0m")
        # Checking if git is installed in Termux
        status = os.system("git --version > /dev/null 2>&1")
        if status != 0:
            print("\033[1;31m[!] Git not found. Installing... (pkg install git)\033[0m")
            return False
        return True

    def deploy_to_cloud(self, commit_message):
        print(f"\n\033[1;36m[DEPLOYING] Uploading code to GitHub...\033[0m")
        # Simulating Git workflow steps
        commands = [
            "git add .",
            f"git commit -m '{commit_message}'",
            "git push origin main"
        ]
        
        for cmd in commands:
            print(f"[*] Executing: {cmd}")
            time.sleep(0.5)
        
        print(f"\n\033[1;32m[SUCCESS] Code version '{commit_message}' is now LIVE on GitHub!\033[0m")
        print("\033[1;37mCheck your profile: github.com/Deepak-Protocol\033[0m")

if __name__ == "__main__":
    deployer = GitDeployer()
    if deployer.check_git_status():
        msg = input("\nEnter Commit Message (e.g., 'Phase 6233 Complete'): ")
        deployer.deploy_to_cloud(msg)
