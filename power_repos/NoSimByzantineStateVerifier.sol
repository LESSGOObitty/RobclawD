// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title NoSimByzantineStateVerifier
 * @notice Direct, deterministic state verification without simulation or trace emulation.
 */
contract NoSimByzantineStateVerifier {
    bytes32 public currentBTreeStateRoot;

    event StateUpdated(bytes32 indexed oldRoot, bytes32 indexed newRoot, bytes32 payloadHash);

    constructor(bytes32 initialRoot) {
        currentBTreeStateRoot = initialRoot;
    }

    /**
     * @notice Applies a pure state transition based on a verified Merkle DAG proof.
     * @param proof Array of sibling hashes along the Merkle path.
     * @param leaf The leaf hash containing the B-Tree state delta.
     * @param newRoot The expected root after updating the state leaf.
     */
    function verifyAndApplyState(
        bytes32[] calldata proof,
        bytes32 leaf,
        bytes32 newRoot
    ) external {
        // Pure inline assembly execution to save gas and avoid EVM call overhead
        assembly {
            let computedHash := leaf
            let proofLength := proof.length
            let proofPtr := proof.offset

            for { let i := 0 } lt(i, proofLength) { i := add(i, 1) } {
                let sibling := calldataload(proofPtr)
                
                // Sort pair hashes deterministically
                switch lt(computedHash, sibling)
                case 1 {
                    mstore(0x00, computedHash)
                    mstore(0x20, sibling)
                }
                default {
                    mstore(0x00, sibling)
                    mstore(0x20, computedHash)
                }

                computedHash := keccak256(0x00, 0x40)
                proofPtr := add(proofPtr, 0x20)
            }

            // Read existing root from storage slot 0
            let currentRoot := sload(currentBTreeStateRoot.slot)

            // Revert if cryptographic proof does not match current state root
            if iszero(eq(computedHash, currentRoot)) {
                // Revert with selector bytes4(keccak256("InvalidProof()"))
                mstore(0x00, 0x09bde33900000000000000000000000000000000000000000000000000000000)
                revert(0x00, 0x04)
            }

            // Commit new B-Tree State Root directly
            sstore(currentBTreeStateRoot.slot, newRoot)
        }

        emit StateUpdated(currentBTreeStateRoot, newRoot, leaf);
    }
}
