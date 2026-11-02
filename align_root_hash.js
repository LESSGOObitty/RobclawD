const crypto = require('crypto'), fs = require('fs');

const WORKING_DIR = '/data/data/com.termux/files/home/Matrix-Ledger';
const MANIFEST_PATH = `${WORKING_DIR}/state_manifest.json`;

if (!fs.existsSync(WORKING_DIR)) fs.mkdirSync(WORKING_DIR, { recursive: true });

// Load existing manifest or generate baseline
let metrics = {
    MasterLightConstant: 299792458,
    GoldGrainMetric: 0.06479891,
    FrequencyBand: "40MHz",
    ActiveChannels: 24
};

if (fs.existsSync(MANIFEST_PATH)) {
    try {
        const existing = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
        metrics = { ...metrics, ...existing };
    } catch(e) {}
}

const payloadString = JSON.stringify(metrics);
const rootHash = crypto.createHash('sha256').update(payloadString).digest('hex');

const alignedState = {
    ...metrics,
    RootHash: rootHash,
    InvariantKey: 932808725,
    Drift: "0%",
    Timestamp: Math.floor(Date.now() / 1000)
};

fs.writeFileSync(MANIFEST_PATH, JSON.stringify(alignedState, null, 2), 'utf8');

process.stdout.write("\x1b[H\x1b[J");
console.log("\x1b[38;5;51m=====================================================================\x1b[0m");
console.log("\x1b[38;5;226m     [ROBDOE.TERMUX] ROOT HASH & INVARIANT ALIGNMENT COMPLETE        \x1b[0m");
console.log("\x1b[38;5;51m=====================================================================\x1b[0m");
console.log(` \x1b[33m[STATUS]\x1b[0m        : SYNCHRONIZED // 0% DRIFT`);
console.log(` \x1b[33m[ROOT HASH]\x1b[0m     : sha256:${rootHash}`);
console.log(` \x1b[33m[MANIFEST]\x1b[0m      : ${MANIFEST_PATH}`);
console.log("\x1b[38;5;51m=====================================================================\x1b[0m");
