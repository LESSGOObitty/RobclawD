import os
import subprocess

HOME_DIR = os.path.expanduser("~")
WORKSPACE_DIR = os.path.expanduser("~/workspace")

def get_git_repos():
    repos = [HOME_DIR]
    if os.path.exists(WORKSPACE_DIR):
        for entry in os.listdir(WORKSPACE_DIR):
            full_path = os.path.join(WORKSPACE_DIR, entry)
            if os.path.isdir(os.path.join(full_path, ".git")):
                repos.append(full_path)
    return repos

def sync_repo(repo_path):
    print(f"[*] Checking repo: {repo_path}")
    try:
        # Check status
        status_res = subprocess.run(["git", "-C", repo_path, "status", "--porcelain"], capture_output=True, text=True, check=True)
        if not status_res.stdout.strip():
            print(f"    -> Clean. No changes to sync.")
            return

        print(f"    -> Changes detected. Staging safely...")
        
        if repo_path == HOME_DIR:
            # For home repo, stage tracked updates and safe workspace subpaths to avoid submodule index errors
            subprocess.run(["git", "-C", repo_path, "add", "-u"], check=True)
            if os.path.exists(WORKSPACE_DIR):
                subprocess.run(["git", "-C", repo_path, "add", "workspace/"], check=True)
        else:
            # For isolated workspace repos
            subprocess.run(["git", "-C", repo_path, "add", "-A"], check=True)
        
        # Check if anything is actually staged before committing
        staged_check = subprocess.run(["git", "-C", repo_path, "diff", "--cached", "--quiet"])
        if staged_check.returncode != 0:
            commit_msg = "chore(guardian): auto-sync state checkpoint"
            subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_msg], check=True)
            
            print(f"    -> Pushing to origin/main...")
            subprocess.run(["git", "-C", repo_path, "push", "origin", "main"], check=True)
            print(f"[+] Successfully synced {repo_path}")
        else:
            print(f"    -> No staged changes to commit.")
            
    except subprocess.CalledProcessError as e:
        print(f"[!] Git sync error in {repo_path}: {e}")
    except Exception as ex:
        print(f"[!] Unexpected error: {ex}")

if __name__ == "__main__":
    print("=== 🛡️ WORKSPACE GIT GUARDIAN ===")
    for repo in get_git_repos():
        sync_repo(repo)
    print("=== SYNC COMPLETE ===")
