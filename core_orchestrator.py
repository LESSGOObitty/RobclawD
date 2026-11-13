#!/data/data/com.termux/files/usr/bin/env python3
"""
RobDoeAI-Core // Decentralized Dynamic Lattice Orchestrator (Rootless / Peer-Agnostic)
Operator: root@robdoe.com (1 of 1 Sovereign Architecture)
"""

import os
import json
import time
import hashlib
import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] [%(name)s] -> %(message)s"
)
logger = logging.getLogger("RobDoeOrchestrator")

class DecentralizedOrchestrator:
    def __init__(self, workspace_path: str):
        self.workspace = workspace_path
        self.state_manifest = {}

    def compute_dynamic_dag_root(self) -> str:
        logger.info("Computing dynamic, rootless decentralized DAG state across all shards & submodules...")
        hasher = hashlib.sha512()
        
        # Walk workspace dynamically, excluding git internal metadata and heavy build artifacts
        for root, dirs, files in os.walk(self.workspace):
            if ".git" in root or "hard_repos" in root:
                # Still incorporate submodule HEAD references for cryptographic entanglement
                continue
            files.sort()
            for file in files:
                if file.endswith((".py", ".json", ".sh", ".md")):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rb") as f:
                            content = f.read()
                            hasher.update(content)
                    except Exception as e:
                        logger.warning(f"Skipped unreadable file {file_path}: {e}")

        # Entangle submodule commit hashes for absolute decentralized consensus
        submodules = ["hard_repos/bitcoin", "hard_repos/linux", "hard_repos/xv6-riscv"]
        for sub in submodules:
            git_file = os.path.join(self.workspace, sub, ".git")
            if os.path.exists(git_file) or os.path.isdir(git_file):
                try:
                    res = subprocess.run(["git", "-C", sub, "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
                    hasher.update(res.stdout.strip().encode("utf-8"))
                    logger.info(f"Entangled Submodule [{sub}] -> {res.stdout.strip()[:12]}")
                except Exception:
                    pass

        dynamic_root = hasher.hexdigest()
        logger.info(f"Dynamic Decentralized Root Computed: {dynamic_root[:32]}...")
        return dynamic_root

    def execute_git_pipeline(self):
        logger.info("Synchronizing decentralized git pipeline with auto-stash resilience...")
        try:
            subprocess.run(["git", "stash"], capture_output=True)
            subprocess.run(["git", "fetch", "origin", "main"], check=True, capture_output=True)
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True, capture_output=True)
            subprocess.run(["git", "stash", "pop"], capture_output=True)
            subprocess.run(["git", "add", "."], check=True, capture_output=True)
            
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
            if status.stdout.strip():
                subprocess.run(["git", "commit", "-m", "refactor(core): elevate to rootless decentralized DAG orchestrator [1 of 1]"], check=True, capture_output=True)
                subprocess.run(["git", "push", "origin", "main"], check=True, capture_output=True)
                logger.info("Decentralized pipeline synchronized and pushed successfully.")
            else:
                logger.info("Working tree pristine. No commits required.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Git pipeline exception: {e.stderr.decode('utf-8', errors='ignore')}")
            raise

    def run(self):
        dynamic_root = self.compute_dynamic_dag_root()
        self.state_manifest = {
            "system": "RobDoeAI-Core // Rootless Decentralized Orchestrator",
            "operator": "root@robdoe.com",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "dynamic_decentralized_root": dynamic_root,
            "status": "ROOTLESS_DAG_ACTIVE"
        }
        
        output_path = "decentralized_orchestration_state.json"
        with open(output_path, "w") as f:
            json.dump(self.state_manifest, f, indent=2)
            
        self.execute_git_pipeline()

if __name__ == "__main__":
    workspace = os.getcwd()
    orchestrator = DecentralizedOrchestrator(workspace)
    orchestrator.run()
