async function main() {
    const [deployer] = await ethers.getSigners();
    console.log(`[*] Anchoring primary asset robdoe.com with account: ${deployer.address}`);
    
    const Registry = await ethers.getContractFactory("Registry");
    const registry = await Registry.deploy();
    await registry.waitForDeployment();
    const registryAddress = await registry.getAddress();
    console.log(`[✔] Registry deployed at: ${registryAddress}`);

    const domain = "robdoe.com";
    const targetHash = ethers.id("ROBDOE_SOVEREIGN_NODE_v1");

    console.log(`[*] Setting record for ${domain}...`);
    const tx = await registry.setRecord(domain, targetHash);
    await tx.wait();

    console.log(`[✔] Record anchored on-chain for ${domain}! Tx Hash: ${tx.hash}`);

    const retrieved = await registry.getRecord(domain);
    console.log(`[✔] Verified Record for ${domain}: ${retrieved}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
