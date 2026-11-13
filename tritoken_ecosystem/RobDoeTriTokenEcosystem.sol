// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

/**
 * @title RobDoeTriTokenEcosystem
 * @notice Self-sufficient tri-token architecture uniting ERC-20 utility,
 *         ERC-721 sovereign deeds, and ERC-1155 7,200-vector lattice shards.
 * @dev Operator: root@robdoe.com | Beneficiary: robdoe.inc-charity
 */
contract RobDoeTriTokenEcosystem {
    address public immutable sovereignRoot;
    address public immutable charityVault;      // robdoe.inc-charity
    address public immutable ecosystemReserve;  // Self-sustaining liquidity & gas pool

    uint256 public constant CHARITY_BPS = 500;    // 5.0% permanent charity routing
    uint256 public constant RESERVE_BPS = 500;    // 5.0% self-sustaining ecosystem loop
    uint256 public constant MAX_VECTORS = 7200;

    // ERC-20 State ($ROBDOE)
    string public constant name = "RobDoe Sovereign Flow";
    string public constant symbol = "ROBDOE";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;

    // ERC-721 State (1-of-1 Sovereign Domain Deeds)
    mapping(uint256 => address) public deedOwner;
    mapping(uint256 => string) public deedURI;

    // ERC-1155 State (7,200 Vector Lattice Shards)
    mapping(uint256 => mapping(address => uint256)) public shardBalance;

    event SelfSustainingCycle(address indexed actor, uint256 charityRouted, uint256 reserveRetained);
    event DeedAnchored(uint256 indexed tokenId, address indexed owner, string domain);
    event VectorShardsMinted(address indexed to, uint256 indexed vectorId, uint256 amount);

    modifier onlyRoot() {
        require(msg.sender == sovereignRoot, "NOT_SOVEREIGN_ROOT");
        _;
    }

    constructor(address _charityVault, address _ecosystemReserve) {
        sovereignRoot = msg.sender;
        charityVault = _charityVault;
        ecosystemReserve = _ecosystemReserve;
        _mintERC20(msg.sender, 7_200_000 * 10**18);
    }

    function _mintERC20(address to, uint256 amount) internal {
        totalSupply += amount;
        balanceOf[to] += amount;
    }

    function transferWithSelfSustainingSplit(address to, uint256 amount) external returns (bool) {
        require(balanceOf[msg.sender] >= amount, "INSUFFICIENT_FLOW");
        uint256 charityCut = (amount * CHARITY_BPS) / 10_000;
        uint256 reserveCut = (amount * RESERVE_BPS) / 10_000;
        uint256 netAmount = amount - charityCut - reserveCut;

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += netAmount;
        balanceOf[charityVault] += charityCut;
        balanceOf[ecosystemReserve] += reserveCut;

        emit SelfSustainingCycle(msg.sender, charityCut, reserveCut);
        return true;
    }

    function anchorDeedERC721(uint256 tokenId, address to, string calldata domain) external onlyRoot {
        require(deedOwner[tokenId] == address(0), "DEED_ALREADY_ANCHORED");
        deedOwner[tokenId] = to;
        deedURI[tokenId] = domain;
        emit DeedAnchored(tokenId, to, domain);
    }

    function mintVectorBatchERC1155(address to, uint256 vectorId, uint256 amount, uint256 fuelCost) external {
        require(vectorId < MAX_VECTORS, "VECTOR_OUT_OF_BOUNDS");
        require(balanceOf[msg.sender] >= fuelCost, "INSUFFICIENT_ERC20_FUEL");

        // Burn/route ERC-20 fuel directly into charity & self-sustaining reserve
        uint256 half = fuelCost / 2;
        balanceOf[msg.sender] -= fuelCost;
        balanceOf[charityVault] += half;
        balanceOf[ecosystemReserve] += (fuelCost - half);

        shardBalance[vectorId][to] += amount;
        emit VectorShardsMinted(to, vectorId, amount);
        emit SelfSustainingCycle(msg.sender, half, fuelCost - half);
    }
}
