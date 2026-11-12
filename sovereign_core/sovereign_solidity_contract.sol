// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title Sovereign Ledger Token (SOL)
 * @dev Air-Gapped, Low-Entropy, Tachyon-Scaled ERC-20 Implementation
 * Total Supply: 1,296,000 anchored to the grand arc sweep.
 */
contract SovereignLedgerToken {
    string public constant name = "Sovereign Ledger Token";
    string public constant symbol = "SOL";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 1296000 * (10 ** uint256(decimals));

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor() {
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address to, uint256 value) public returns (bool) {
        require(balanceOf[msg.sender] >= value, "SOL: Insufficient sovereign balance");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) public returns (bool) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        require(balanceOf[from] >= value, "SOL: Insufficient balance");
        require(allowance[from][msg.sender] >= value, "SOL: Insufficient allowance");
        balanceOf[from] -= value;
        balanceOf[to] += value;
        allowance[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }
}
