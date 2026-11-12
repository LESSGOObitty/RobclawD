import os, json, hashlib, time

BASE_DIR = os.path.expanduser("~")
PROVMARK_DIR = os.path.join(BASE_DIR, ".provmark")
QUICKDRAW_LOG = os.path.join(PROVMARK_DIR, "quickdraw_achievement.json")

def seal_quickdraw():
    timestamp = int(time.time())
    
    # Metadata from Quickdraw achievement screen
    achievement = "Quickdraw"
    tagline = "Gitty up!"
    unlock_date = "11 September"
    repo_target = "robdoeeaiagency101/demo-repository #1"
    metric = "Closed within 5 minutes of opening"
    
    raw_seed = f"{achievement}_{repo_target}_{unlock_date}_{timestamp}"
    hash_256 = hashlib.sha256(raw_seed.encode()).hexdigest()
    
    payload = {
        "authority": "robdoe.com",
        "timestamp": timestamp,
        "achievement": achievement,
        "tagline": tagline,
        "unlocked_date": unlock_date,
        "repository": repo_target,
        "performance_metric": metric,
        "sha256_root": hash_256,
        "status": "ACHIEVEMENT_SEALED"
    }
    
    os.makedirs(PROVMARK_DIR, exist_ok=True)
    with open(QUICKDRAW_LOG, "w") as f:
        json.dump(payload, f, indent=2)
        
    print("========================================================================")
    print(" [ROBDOE.COM] QUICKDRAW ACHIEVEMENT SEALED")
    print("========================================================================")
    print(f" [+] Target Repo      : {repo_target}")
    print(f" [+] Metric           : {metric}")
    print(f" [+] Unlock Date      : {unlock_date}")
    print(f" [+] SHA-256 Root     : {hash_256[:32]}...")
    print(f" [✓] Status           : GITTY UP & LOCKED")
    print("========================================================================")

if __name__ == "__main__":
    seal_quickdraw()
