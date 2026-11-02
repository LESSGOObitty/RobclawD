// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract LocalERC1155Anchor {
    mapping(uint256 => mapping(address => uint256)) private _balances;
    string private _uri;

    event TransferSingle(address indexed operator, address indexed from, address indexed to, uint256 id, uint256 value);

    constructor(string memory uri_) {
        _uri = uri_;
    }

    function mint(address account, uint256 id, uint256 amount, bytes memory data) public {
        _balances[id][account] += amount;
        emit TransferSingle(msg.sender, address(0), account, id, amount);
    }

    function balanceOf(address account, uint256 id) public view returns (uint256) {
        return _balances[id][account];
    }
}
