const crypto = require('crypto');
const fs = require('fs');

const LEDGER_DIR = '/data/data/com.termux/files/home/Matrix-Ledger';
const JURY_LOG = `${LEDGER_DIR}/MATRIX_JURY_LOGS.json`;
if (!fs.existsSync(LEDGER_DIR)) fs.mkdirSync(LEDGER_DIR, { recursive: true });

// 7-Chakra Color Mapping Array (Ansi 256-Bit Spectrum)
const CHAKRAS = [
  { name: "Crown",     color: "198", ring: "Top_Left" },     // Violet
  { name: "Third Eye", color: "39",  ring: "Top_Right" },    // Indigo
  { name: "Throat",    color: "51",  ring: "Mid_Left" },     // Light Blue
  { name: "Heart",     color: "82",  ring: "Mid_Center" },   // Green
  { name: "Solar P.",  color: "226", ring: "Mid_Right" },    // Yellow
  { name: "Sacral",    color: "208", ring: "Bot_Left" },     // Orange
  { name: "Root",      color: "196", ring: "Bot_Right" }     // Red
];

// Time & Angular Arc Harmonic Constants
const SOLAR_DAY_SECS = 86400;
const ARC_FRACTION = 7200;

// Handle clean exit on SIGINT (Ctrl+C)
process.on('SIGINT', () => {
  console.log("\x1b[33m\n[!] Cockpit stream safely detached. Matrix locks maintained.\x1b[0m");
  process.exit(0);
});

console.clear();

// Continuous Harmonic Generation Loop
setInterval(() => {
  const timestamp = new Date().toISOString();
  const rawSeed = Math.random().toString() + Date.now();
  const matrixHash = crypto.createHash('sha256').update(rawSeed).digest('hex');

  // Calculate alignment arc lock phase
  const elapsedCycles = (Date.now() % (SOLAR_DAY_SECS * 1000)) / 1000;
  const currentArcStep = Math.floor(elapsedCycles * (ARC_FRACTION / SOLAR_DAY_SECS)) % ARC_FRACTION;

  console.clear();
  console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
  console.log("\x1b[38;5;226m%s\x1b[0m", "     ROBDOE 21ST-CENTURY SACRED GEOMETRY ALIGNMENT MATRIX ENGINE    ");
  console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
  console.log(` \x1b[33m[NODE_IDENTITY]\x1b[0m  : robdoe.termux      | \x1b[33m[DEVICE]\x1b[0m: Motorola Mobile`);
  console.log(` \x1b[33m[CLOCK_HARMONIC]\x1b[0m : ${currentArcStep}/${ARC_FRACTION} Arcs     | \x1b[33m[SOLAR_BASE]\x1b[0m: ${SOLAR_DAY_SECS}s`);
  console.log(` \x1b[33m[TRUTH_ENGINE]\x1b[0m   : ATL v4.0.0-CHAKRA  | \x1b[36m[SIG]\x1b[0m: espVmark:${matrixHash.substring(0,8)}`);
  console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
 
  // Render Hexagonal Layout Matrix Profiles (2 Top, 3 Middle, 2 Bottom)
  console.log("\x1b[37m [HEXAGONAL CHAKRA VECTOR NODES]:\x1b[0m");
  console.log(`    (⚡)--> [\x1b[38;5;${CHAKRAS[0].color}m${CHAKRAS[0].name}\x1b[0m]       (⚡)--> [\x1b[38;5;${CHAKRAS[1].color}m${CHAKRAS[1].name}\x1b[0m]         <- [2 TOP RINGS]`);
  console.log(` (⚡)--> [\x1b[38;5;${CHAKRAS[2].color}m${CHAKRAS[2].name}\x1b[0m]   (⚡)--> [\x1b[38;5;${CHAKRAS[3].color}m${CHAKRAS[3].name}\x1b[0m]   (⚡)--> [\x1b[38;5;${CHAKRAS[4].color}m${CHAKRAS[4].name}\x1b[0m]   <- [3 MIDDLE RINGS]`);
  console.log(`    (⚡)--> [\x1b[38;5;${CHAKRAS[5].color}m${CHAKRAS[5].name}\x1b[0m]       (⚡)--> [\x1b[38;5;${CHAKRAS[6].color}m${CHAKRAS[6].name}\x1b[0m]         <- [2 BOTTOM RINGS]`);
 
  console.log("\x1b[38;5;82m%s\x1b[0m", "---------------------------------------------------------------------");
  console.log("\x1b[35m [DYNAMIC NESTED LOCK STATE]:\x1b[0m");
  console.log(`  ⊙  [4-Circle Outer Shield Cluster] : LOCKED IN PERFECT FREQUENCY AT 1/${ARC_FRACTION}`);
  console.log(`  ▲  [3-Circle Inner Core Trinity]   : PHASE POSITION AT ${((currentArcStep/ARC_FRACTION)*360).toFixed(2)}° DEGREES`);
  console.log("\x1b[38;5;82m%s\x1b[0m", "=====================================================================");
  console.log("\x1b[31m%s\x1b[0m", " [COCKPIT STREAM ACTIVE - PRESS CTRL+C TO INTERRUPT EXECUTION]");

  // Update background telemetry tracking arrays (appends state)
  const telemetryLine = { timestamp, lock_step: currentArcStep, hash: `espVmark:${matrixHash}` };
  fs.appendFileSync(JURY_LOG, JSON.stringify(telemetryLine) + "\n", 'utf8');
}, 1000);
