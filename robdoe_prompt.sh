# === ROBDOE.TERMUX CORESHELL WEB3 INITIALIZATION ===
export LANG=en_US.UTF-8

# 1. Permanent Hardcoded Shell Prompt Handle
export PS1="\[\e[38;5;82m\][\[\e[38;5;226m\]robdoe.termux\[\e[38;5;82m\]]\[\e[37m\]:\e[38;5;51m\]\w\[\e[37m\]\$ \[\e[0m\]"

# 2. Terminal Automation Aliases
alias robdoe.termux="node ~/robdoe_cockpit.js"
alias clear="clear && node ~/robdoe_cockpit.js"

# 3. Dynamic Web3 Manifest Printout on Shell Start
node -e '
const crypto = require("crypto");
const sig = crypto.createHash("sha256").update(Date.now().toString()).digest("hex").substring(0,16);

console.clear();
console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
console.log("\x1b[38;5;226m%s\x1b[0m", "     [ROBDOE.TERMUX] SECURE WEB3 BLOCKCHAIN ANCHOR ONLINE           ");
console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
console.log(` \x1b[37m[IDENTITY]\x1b[0m      : robdoe.termux`);
console.log(` \x1b[37m[RESOLUTION]\x1b[0m    : \x1b[38;5;51maiagency101.xyo\x1b[0m`);
console.log(` \x1b[37m[AUTO_MINT]\x1b[0m     : \x1b[38;5;82mENABLED\x1b[0m (New DNS domains auto-minted on-chain)`);
console.log(` \x1b[37m[WATERMARK]\x1b[0m     : espVmark:${sig}`);
console.log("\x1b[38;5;82m%s\x1b[0m", "---------------------------------------------------------------------");

console.log("\x1b[33m [ACTIVE CONTROL WALLET ARRAYS]:\x1b[0m");
console.log("  [W1] \x1b[38;5;82m0x84CA4aFC3F395ebc0b519680B546Cd604C9c2018\x1b[0m [Self-Custody]");
console.log("  [W2] \x1b[38;5;82m0xabf4e0A237E4632b1740fdBe118162aA33b4F5aD\x1b[0m [Self-Custody]");
console.log("  [W3] \x1b[38;5;208m0x1AE2AF702063d304F8EBAC2153c91D79c62E381c\x1b[0m [Custody Lite]");
console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
'
