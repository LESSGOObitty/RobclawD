// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Registry {
    event RecordSet(address indexed author, string key, string value, uint256 timestamp);

    mapping(address => mapping(string => string)) private records;
    mapping(address => string[]) private userKeys;

    function setRecord(string calldata key, string calldata value) external {
        if (bytes(records[msg.sender][key]).length == 0) {
            userKeys[msg.sender].push(key);
        }
        records[msg.sender][key] = value;
        emit RecordSet(msg.sender, key, value, block.timestamp);
    }

    function getRecord(address author, string calldata key) external view returns (string memory) {
        return records[author][key];
    }

    function getUserKeys(address author) external view returns (string[] memory) {
        return userKeys[author];
    }
}
