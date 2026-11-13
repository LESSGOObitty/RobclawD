import json
import time

manifest = {
    "system": "RobDoeAI-Core // Hardcore Repo Ingestion Lattice",
    "operator": "root@robdoe.com",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "ingested_repos": [
        {"name": "xv6-riscv", "desc": "MIT teaching kernel — raw C and RISC-V assembly"},
        {"name": "linux", "desc": "The Linux Kernel mainline — millions of lines of pure systems grit"},
        {"name": "bitcoin", "desc": "Bitcoin Core — C++ cryptographic consensus engine"}
    ],
    "status": "INGESTED_AND_BOUND"
}

with open("hard_repos_manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(" [+] Hard repos manifest generated.")
