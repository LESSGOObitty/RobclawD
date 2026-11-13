import json
import time

state = {
    "system": "RobDoeAI-Core // Stash Rebase Reconciliation",
    "operator": "root@robdoe.com",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "status": "STASH_REBASE_PUSH_COMPLETE"
}

with open("stash_recovery_state.json", "w") as f:
    json.dump(state, f, indent=2)

print(" [+] Stash recovery state recorded.")
