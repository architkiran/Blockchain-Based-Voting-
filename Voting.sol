// Voting.sol
pragma solidity ^0.5.16;

contract Voting {
    mapping(address => bool) public voters;
    mapping(string => uint256) public votesReceived;

    event VoteCast(address indexed voter, string candidate);

    function vote(string memory candidate) public {
        require(!voters[msg.sender], "You have already voted.");
        voters[msg.sender] = true;
        votesReceived[candidate]++;
        emit VoteCast(msg.sender, candidate);
    }

    function getVotesForCandidate(string memory candidate) public view returns (uint256) {
        return votesReceived[candidate];
    }
}
