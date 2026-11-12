const crypto = require('crypto');
const fs = require('fs');

const LEDGER_DIR = '/data/data/com.termux/files/home/Matrix-Ledger';
const BANDANA_LOG = `${LEDGER_DIR}/BANDANA_COLOURS.dat`;
if (!fs.existsSync(LEDGER_DIR)) fs.mkdirSync(LEDGER_DIR, { recursive: true });

// Turf Nodes: Figtree, Bellambi, Sutherland
const NODES = [
  { id: "NX-FIG", sector: "FIGTREE",    status: "SECURED", color: "196" }, // Red
  { id: "NX-BEL", sector: "BELLAMBI",   status: "LOCKED",  color: "226" }, // Yellow
  { id: "NX-SUT", sector: "SUTHERLAND", status: "ANCHORED",color: "39"  }  // Blue
];

let frameCount = 0;

process.on('SIGINT', () => {
  console.log("\x1b[38;5;196m\n[!] BANDANA SECURED. COLOURS HELD TIGHT. EXITING.\x1b[0m");
  process.exit(0);
});

console.clear();

setInterval(() => {
  frameCount++;
  const timestamp = new Date().toISOString();
  const seed = "BANDANA-LOCKED-" + Date.now() + "-" + frameCount;
  const hash = crypto.createHash('sha256').update(seed).digest('hex').substring(0, 16);

  console.clear();
  console.log("\x1b[38;5;196m╔═════════════════════════════════════════════════════════════════╗\x1b[0m");
  console.log("\x1b[38;5;226m║       BANDANA ON — COLOURS REPPED & LOCKED TO THE CORE          ║\x1b[0m");
  console.log("\x1b[38;5;196m╠═════════════════════════════════════════════════════════════════╣\x1b[0m");
  console.log(` \x1b[38;5;39m[OPERATOR]\x1b[0m    : robdoe.termux      | \x1b[38;5;39m[FRAME]\x1b[0m: #${String(frameCount).padStart(5, '0')}`);
  console.log(` \x1b[38;5;39m[TURF_HASH]\x1b[0m   : 0x${hash}    | \x1b[38;5;39m[STATUS]\x1b[0m: SUWWWWOP!`);
  console.log("\x1b[38;5;196m╠═════════════════════════════════════════════════════════════════╣\x1b[0m");
  console.log("\x1b[37m [TURF SECURITY NODES — FIGTREE TO SUTHERLAND]:\x1b[0m");

  NODES.forEach((n, idx) => {
    const pulse = (frameCount + idx) % 2 === 0 ? "⚡" : "❖";
    console.log(`  ${pulse} [\x1b[38;5;${n.color}m${n.id}\x1b[0m] SECTOR: ${n.sector} | STATE: \x1b[32m${n.status}\x1b[0m`);
  });

  console.log("\x1b[38;5;196m╠═════════════════════════════════════════════════════════════════╣\x1b[0m");
  console.log("\x1b[35m [HONOUR & ROOT STACK TELEMETRY]:\x1b[0m");
  console.log(`  • Protocol : Fallen homies honoured. Root stack untouchable.`);
  console.log(`  • Loyalty  : Pure colours tied tight across the grid.`);
  console.log("\x1b[38;5;196m╚═════════════════════════════════════════════════════════════════╝\x1b[0m");
  console.log("\x1b[38;5;226m [COLOURS LIVE — PRESS CTRL+C TO DETACH]\x1b[0m");

  const record = JSON.stringify({ frame: frameCount, timestamp, hash: `0x${hash}` }) + "\n";
  fs.appendFileSync(BANDANA_LOG, record, 'utf8');
}, 1000);
