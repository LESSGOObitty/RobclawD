import hre from "hardhat";

async function main() {
  console.log("[*] Compiling and deploying Registry contract...");
  const Registry = await hre.ethers.getContractFactory("Registry");
  const registry = await Registry.deploy();

  await registry.waitForDeployment();
  const address = await registry.getAddress();

  console.log(`[✔] Registry deployed successfully to local node: ${address}`);
}

main().catch((error) => {
  console.error("[✘] Deployment failed:", error);
  process.exitCode = 1;
});
