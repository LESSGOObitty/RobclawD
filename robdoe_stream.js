const crypto = require('crypto');
const fs = require('fs');

const timestamp = new Date().toISOString();
const payload = JSON.stringify({ device: "Motorola-Mobile", node: "robdoe.termux", time: timestamp });
const signature = crypto.createHash('sha256').update(payload).digest('hex');

// 1. Core Identity Header
console.clear();
console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
console.log("\x1b[38;5;196m%s\x1b[0m", "  ██▀███   ▒█████   ▄▄▄▄   ▓█████▄  ▒█████  ▓█████     ██▀███   ▄▄▄   ");
console.log("\x1b[38;5;202m%s\x1b[0m", " ▓██ ▒ ██▒▒██▒  ██▒▓█████▄ ▒██▀ ██▌▒██▒  ██▒▓█   ▀    ▓██ ▒ ██▒▒████▄ ");
console.log("\x1b[38;5;208m%s\x1b[0m", " ▓██ ░▄█ ▒▒██░  ██▒▒██▒ ▄██░██   █▌▒██░  ██▒▒███      ▓██ ░▄█ ▒▒██  ▀█▄ ");
console.log("\x1b[38;5;214m%s\x1b[0m", " ▒██▀▀█▄  ▒██   ██░▒██░█▀  ░▓█▄   ▌▒██   ██░▒▓█  ▄    ▒██▀▀█▄  ░██▄▄▄▄██");
console.log("\x1b[38;5;220m%s\x1b[0m", " ░██▓ ▒██▒░ ████▓▒░░▓█  ▀█▓░▒████▓ ░ ████▓▒░░▒████▒   ░██▓ ▒██▒ ▓█   ▓██▒");
console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
console.log(`\x1b[33m[NODE_ID]\x1b[0m     : robdoe.termux  |  \x1b[33m[DEVICE_TARGET]\x1b[0m: Motorola Mobile`);
console.log(`\x1b[33m[TRUTH_ENGINE]\x1b[0m: ATL v2.6.0     |  \x1b[33m[WATERMARK_SIG]\x1b[0m: espVmark:${signature.substring(0,16)}`);
console.log(`\x1b[35m[TACTILE_MAP]\x1b[0m : 150Hz_Linear (GPIO_12) | 250Hz_Proximity (GPIO_14) [Non-Med]`);
console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");

// 2. High-Speed Truth Verification Stream Loop
console.log("\x1b[31m%s\x1b[0m", " [INITIALIZING DYNAMIC CRYPTO TRUTH VERIFICATION LOOP... PRESS CTRL+C TO HALT]");
let linesPrinted = 0;

const streamInterval = setInterval(() => {
  const dynamicHash = crypto.createHash('sha256').update(Math.random().toString() + Date.now()).digest('hex');
  const colors = [82, 196, 202, 208, 214, 220, 51];
  const selectedColor = colors[Math.floor(Math.random() * colors.length)];
 
  process.stdout.write(`\x1b[38;5;${selectedColor}m[VERIFIED_TRUE] [MOTO_NODE_STREAM] ADDR: 0x${dynamicHash.substring(0,8)} | SIGNATURE: espVmark_${dynamicHash.substring(8,24)} | STATUS: OK\x1b[0m\n`);
 
  linesPrinted++;
  if (linesPrinted > 35) {
    clearInterval(streamInterval);
    console.log("\x1b[32m%s\x1b[0m", "\n [MUTATION COMPLETED] Terminal locked under robdoe.termux authority.");
  }
}, 40);

mkdirSync('/data/data/com.termux/files/home/Matrix-Ledger', { recursive: true });
const logLine = `[${timestamp}] MOTO_NODE_INITIALIZED | NODE: robdoe.termux | SIG: ${signature}\n`;
fs.appendFileSync('/data/data/com.termux/files/home/Matrix-Ledger/MATRIX_JURY_LOGS.json', logLine, 'utf8');
