# THE GUERRILLA & ANXIETY COOKBOOK
## Bare-Metal Survivalism, Air-Gapped State Machines, & Terminal Sovereignty
*By: Rob Doe / Termux Operational Command*

---

### CHAPTER 1: THE PANIC ROOM ARCHITECTURE
When the cloud goes down, external APIs throttle, and external dependencies fail, sovereignty isn't a philosophy—it's a requirement. This chapter details how to anchor an air-gapped terminal environment on Android using Termux, stripping away unnecessary telemetry and establishing absolute ownership over your hardware state.

* **The Android Air-Gap Doctrine:** Operating from an isolated device (such as an air-gapped Moto G) with radios silenced or physically disabled.
* **Directory Hygiene:** Structuring the `~/.merklizer/` B-tree local state stores to maintain zero reliance on external SQL engines or hosted infrastructure.
* **Environment Bootstrapping:** Setting up persistent shell loops, POSIX-compliant paths, and strict execution flags (`set -euo pipefail`) to ensure daemon stability.

---

### CHAPTER 2: THE ANXIETY LOOP (ENTROPY & HARDWARE TAPPING)
When physical serial busses drop or hardware sensors go offline, your state machine cannot afford to block or hang. You need an alternate pulse.

* **Handling Dead Serial Busses:** Gracefully detecting when `/dev/ttyUSB0` drops and instantly switching to a simulated or alternative hardware feedback loop.
* **Backdoor Noise Ingestion:** Siphoning raw kernel entropy directly from `/dev/urandom` and reading `/proc/sys/kernel/random/entropy_avail` to maintain continuous rhythm.
* **Frequency Grounding:** Mapping high-entropy byte arrays into stable frequency and RPM vectors (e.g., maintaining a steady 30–60 Hz heartbeat) to calm the system architecture.

---

### CHAPTER 3: SOLVENCY & PARANOIA (EIP-140 & BYZANTIUM GUARDS)
Financial and state-machine solvency cannot rely on trust; it must be enforced by local code execution.

* **The EIP-140 Revert Guard:** Implementing strict opcode-level conditional checks that trigger instant safe reverts (`REVERT_TRIGGERED_EIP140`) if collateral ratios drop below solvency thresholds.
* **SQLite as a Bunker:** Using local, atomic SQLite databases to log timestamps, equity scores, collateral ratios, and SHA-512 cryptographic seals.
* **Input Sanitization:** Stripping untrusted external vectors through strict regex and modulo arithmetic before they ever touch core ledger logic.

---

### CHAPTER 4: THE SHED DASHBOARD & PROCESS HEALTH
Monitoring a multi-threaded bash architecture requires lightweight, zero-bloat visibility tools.

* **The `ps -ef` Survival Check:** Scanning active background daemons (`master_shed_node.sh`, `external_noise_node.sh`, `shed_entropy_engine.sh`) to verify zero process leakage.
* **Database Table Audits:** Programmatically verifying active SQLite table structures across all `.db` files in the `.merklizer` directory.
* **The `Ctrl+C` Discipline:** Mastering clean process interruption and instant recovery loops without corrupting B-tree ledgers.

---

### CHAPTER 5 THROUGH 17: ADVANCED DAEMON ORCHESTRATION & FIELD NOTES
*(The remaining chapters cover multi-node ESP32 serial telemetry links, local LLM orchestration via Ollama on port 11434, IPFS content-addressed state archiving, and emergency field deployment protocols for mobile terminals).*


---

### CHAPTER 3: SOLVENCY & PARANOIA (EIP-140 & BYZANTIUM GUARDS)
When ledger integrity is paramount and external validation nodes are untrusted, you must rely on cryptographic state seals and zero-knowledge proofs computed locally on the iron.

* **EIP-140 REVERT Integration:** Enforcing strict opcode handling in local EVM state machines to immediately purge invalid state transitions without bleeding side-channel information.
* **Byzantium Merkle Proofs:** Constructing local 72-pool Merkle B-tree ledgers under `~/.merklizer/pools/`, ensuring that historical logs cannot be tampered with post-execution.
* **Local Seal Verification:** Running offline symmetry audits via `merklizer --audit --seal-verify` to confirm that directory states map cleanly to root cryptographic hashes.


---

### CHAPTER 4: THE SHED DASHBOARD & PROCESS HEALTH
Monitoring a multi-threaded bash architecture requires lightweight, zero-bloat visibility tools that never phone home.

* **The `ps -ef` Survival Check:** Scanning active background daemons (`master_shed_node.sh`, `external_noise_node.sh`, `shed_entropy_engine.sh`) to verify zero process leakage across pts channels.
* **Database Table Audits:** Programmatically verifying active SQLite table structures across all `.db` files in the `~/.merklizer/` directory to ensure atomic write integrity.
* **The `Ctrl+C` Discipline:** Mastering clean process interruption and instant recovery loops without corrupting local B-tree ledgers or dangling file descriptors.

---

### CHAPTER 5: ESP32 HARDWARE BRIDGING & SERIAL PROTOCOLS
When moving from purely internal PRNG entropy to physical sensor arrays, the serial bridge becomes your lifeline.

* **Baud Rate Optimization:** Locking hardware UART communication at `115200` baud to minimize buffer latency while preventing packet collisions.
* **Loopback Fallbacks:** Implementing automatic fallback logic that detects dropped USB serial paths (`/dev/ttyUSB0`) and instantly hot-swaps to thermal kernel noise generators.
* **Raw Stream Filtering:** Using `grep`, `awk`, and regex pipelines to strip noise artifacts and extract pure floating-point frequency values from raw hardware strings.

---

### CHAPTER 6: LOCAL LLM OFF-GRID ORCHESTRATION (OLLAMA & TERMUX)
When you need local intelligence without cloud API keys or telemetry leaks, you bring the model directly to the iron.

* **Local Inference via Port 11434:** Running quantized lightweight models locally in Termux to parse telemetry logs and diagnose ledger anomalies in real-time.
* **Air-Gapped Prompts:** Feeding SQLite summary tables directly into local model standard input to generate operational summaries completely offline.
* **Resource Constraint Management:** Balancing CPU thread allocation and memory overhead between active background daemons and local inference engines.


---

### CHAPTER 7: IPFS CONTENT-ADDRESSED STATE ARCHIVING
When centralized servers disappear or local drives face catastrophic failure, your state must be preserved via cryptographically verifiable content addressing.

* **Content Identifiers (CIDs) on the Iron:** Generating local IPFS blocks for SQLite ledger dumps, ensuring that historical states are immutable and globally verifiable.
* **Air-Gapped Pinning Strategies:** Maintaining local node peering without relying on public gateways or hosted pinning services.
* **Hash Verification Loops:** Automatically cross-referencing local Merkle roots against distributed IPFS DAG nodes upon every system boot.

---

### CHAPTER 8: EMERGENCY FIELD PROTOCOLS & RAPID WIPE
When operating in hostile or unstable environments, physical device security and rapid state sanitization are paramount.

* **The Zero-Trace Shutdown:** Executing single-command memory scrubbing and SQLite journal purging to ensure zero forensic footprint remains on the device.
* **Encrypted Volume Dismantling:** Instantly unmounting `.merklizer` encrypted loops and dropping kernel keys from active memory.
* **Hardware Disposal & Extraction:** Protocols for safely dumping cryptographic seed states onto physical media or executing immediate dead-man switches before physical seizure.


---

### CHAPTER 9: ZSH & BASH SCRIPTING HARDENING
Writing scripts for survivalist terminal environments means zero tolerance for unhandled errors, missing dependencies, or silent failures.

* **Strict Execution Flags:** Enforcing `set -euo pipefail` across every script to ensure pipelines abort immediately upon the first anomalous return code or unbound variable.
* **Atomic File Writes:** Writing state updates to temporary staging files before executing atomic `mv` operations to prevent half-written SQLite ledgers during power loss.
* **Signal Traps (`trap`):** Interleaving clean exit handlers (`SIGINT`, `SIGTERM`) to release file locks, flush WAL journals, and restore terminal echo states cleanly.

---

### CHAPTER 10: SERIAL-OVER-RADIO TELEMETRY & NRF24 MODULES
When physical wires are cut and USB serial ports are out of reach, wireless packet transmission over low-frequency radio modules keeps nodes linked.

* **SPI Bus Configuration:** Interfacing ESP32 and Arduino nodes via SPI to NRF24L01+ transceiver modules directly from mobile terminal toolchains.
* **Packet Framing & Checksums:** Wrapping raw telemetry strings in lightweight header-payload-crc frames to discard corrupted radio bursts over noisy atmospheric channels.
* **Frequency Hopping Spread Spectrum (FHSS):** Shifting operational channels dynamically to evade localized RF interference and maintain clandestine node-to-node visibility.

---

### CHAPTER 11: OFFLINE REPOSITORY SOVEREIGNTY & AIR-GAPPED GITHUB MIRRORS
Never depend on live internet connectivity or remote origin servers when you need to rebuild or audit your toolchain from scratch.

* **Local Bare Git Bundles:** Storing compressed, single-file repository bundles (`.bundle`) locally on device for instant cloning without remote fetches.
* **Master SHA-512 Root Hashing:** Generating cryptographic checksum manifests for every script, binary, and documentation file in your offline workspace.
* **Air-Gapped Moto G Mirroring:** Maintaining a fully functional, read-only mirror of core automation repos on an isolated secondary device via local ad-hoc Wi-Fi or USB tethering.

---

### CHAPTER 12: MEMORY MANAGEMENT & RESOURCE THROTTLING ON MOBILE IRON
Running multiple background bash daemons, SQLite connections, and local LLM instances on mobile hardware requires aggressive resource discipline.

* **Cgroup & Nice Priority Tuning:** Assigning lower CPU scheduling priorities (`renice`, `ionice`) to background entropy daemons to keep the active terminal snappy and responsive.
* **RAM Footprint Optimization:** Monitoring RSS and virtual memory consumption via `ps` loops to prevent Android's OOM (Out-Of-Memory) killer from slaughtering critical state daemons mid-ledger write.
* **Disk I/O Batch


---

### CHAPTER 9: ZSH & BASH SCRIPTING HARDENING
Writing scripts for survivalist terminal environments means zero tolerance for unhandled errors, missing dependencies, or silent failures.

* **Strict Execution Flags:** Enforcing `set -euo pipefail` across every script to ensure pipelines abort immediately upon the first anomalous return code or unbound variable.
* **Atomic File Writes:** Writing state updates to temporary staging files before executing atomic `mv` operations to prevent half-written SQLite ledgers during power loss.
* **Signal Traps (`trap`):** Interleaving clean exit handlers (`SIGINT`, `SIGTERM`) to release file locks, flush WAL journals, and restore terminal echo states cleanly.

---

### CHAPTER 10: SERIAL-OVER-RADIO TELEMETRY & NRF24 MODULES
When physical wires are cut and USB serial ports are out of reach, wireless packet transmission over low-frequency radio modules keeps nodes linked.

* **SPI Bus Configuration:** Interfacing ESP32 and Arduino nodes via SPI to NRF24L01+ transceiver modules directly from mobile terminal toolchains.
* **Packet Framing & Checksums:** Wrapping raw telemetry strings in lightweight header-payload-crc frames to discard corrupted radio bursts over noisy atmospheric channels.
* **Frequency Hopping Spread Spectrum (FHSS):** Shifting operational channels dynamically to evade localized RF interference and maintain clandestine node-to-node visibility.

---

### CHAPTER 11: OFFLINE REPOSITORY SOVEREIGNTY & AIR-GAPPED GITHUB MIRRORS
Never depend on live internet connectivity or remote origin servers when you need to rebuild or audit your toolchain from scratch.

* **Local Bare Git Bundles:** Storing compressed, single-file repository bundles (`.bundle`) locally on device for instant cloning without remote fetches.
* **Master SHA-512 Root Hashing:** Generating cryptographic checksum manifests for every script, binary, and documentation file in your offline workspace.
* **Air-Gapped Moto G Mirroring:** Maintaining a fully functional, read-only mirror of core automation repos on an isolated secondary device via local ad-hoc Wi-Fi or USB tethering.

---

### CHAPTER 12: MEMORY MANAGEMENT & RESOURCE THROTTLING ON MOBILE IRON
Running multiple background bash daemons, SQLite connections, and local LLM instances on mobile hardware requires aggressive resource discipline.

* **Cgroup & Nice Priority Tuning:** Assigning lower CPU scheduling priorities (`renice`, `ionice`) to background entropy daemons to keep the active terminal snappy and responsive.
* **RAM Footprint Optimization:** Monitoring RSS and virtual memory consumption via `ps` loops to prevent Android's OOM (Out-Of-Memory) killer from slaughtering critical state daemons mid-ledger write.
* **Disk I/O Batching:** Tuning SQLite PRAGMA settings (`PRAGMA synchronous = NORMAL;`, `PRAGMA journal_mode = WAL;`) to minimize flash storage wear and accelerate transaction speeds.

---

### CHAPTER 13: THE SOVEREIGN SYSTEM CHECK & FINAL FIELD DEPLOYMENT
Bringing the entire architecture together into a single, cohesive, self-healing operational loop ready for deployment in the field.

* **Master Orchestration Wrapper:** Launching all daemons, entropy engines, and dashboard monitors via a single master boot script (`sovereign_init.sh`).
* **Automated Symmetry Audits:** Running continuous cron or background loop checks to verify that local B-tree directories match active database rows and SHA-512 seals.
* **Final Operational Readiness:** Verifying that the terminal state is 100% air-gapped, zero-telemetry, and fully sovereign—ready for whatever the grid throws your way.


---

### CHAPTER 14: MULTI-DAEMON CONCURRENCY & IPC SOCKETS
When your background architecture expands beyond simple cron loops, inter-process communication (IPC) and UNIX domain sockets become essential for synchronized state updates without network overhead.

* **UNIX Domain Sockets in Bash:** Using `nc` (netcat) or `socat` over local socket files in `~/.merklizer/sockets/` to pass encrypted state payloads between the Master node and auxiliary entropy workers.
* **Non-Blocking Pipe Operations:** Configuring file descriptors with non-blocking I/O flags to ensure that a stalled helper daemon never locks up the master execution thread.
* **State Locking & Semaphore Files:** Implementing lightweight PID-file and lock-directory checks (`mkdir` atomic locking) to prevent race conditions when multiple daemons attempt to flush to the same SQLite ledger simultaneously.

---

### CHAPTER 15: FIELD RECOVERY & COLD-START RESTORATION
When your mobile iron suffers an unexpected power loss, kernel panic, or forced reboot, a true sovereign terminal must restore its complete B-tree and ledger state without human intervention.

* **Automated WAL Recovery:** Enforcing automatic SQLite Write-Ahead Log checkpoints upon startup to replay uncommitted transactions and restore database integrity instantly.
* **Merkle Root Re-indexing:** Scanning all ledger directories on boot to rebuild the cryptographic hash tree and verify that no blocks were corrupted during the outage.
* **One-Shot Recovery Script (`boot_restore.sh`):** A single idempotent initialization sequence that verifies environment dependencies, checks storage mounts, validates SQLite schemas, and resurrects all background daemons in correct dependency order.

---

### CHAPTER 16: AIR-GAPPED AUDITING & PROOF VERIFICATION
True sovereignty requires the ability to mathematically prove that your local state has not been tampered with, audited by an external entity, or corrupted by transient memory errors.

* **Offline Cryptographic Audits:** Running local Python or bash verification routines that walk the entire B-tree structure, recomputing SHA-512 hashes and comparing them against stored root seals.
* **Byzantium Proof Generation:** Exporting verifiable ledger subsets into standalone verification bundles that can be transferred via USB OTG or QR code to an air-gapped verification node.
* **Zero-Knowledge State Validation:** Ensuring that state verification confirms solvency and integrity without leaking sensitive transaction metadata or operational parameters.

---

### CHAPTER 17: THE TERMINAL MANIFESTO — LIVING OFF THE GRID
The final doctrine of the Guerrilla & Anxiety Cookbook: maintaining operational readiness, absolute privacy, and total command over your hardware environment regardless of external disruptions.

* **The Zero-Cloud Guarantee:** A permanent commitment to local storage, offline computation, and direct hardware control over every byte of your digital life.
* **Continuous Hardening:** Treating your terminal environment as a living, evolving organism that constantly self-audits, self-seals, and adapts to changing threat models.
* **Final Operational Seal:** Storing the master SHA-512 root hash of your entire operational suite in offline memory. You are now fully sovereign.

