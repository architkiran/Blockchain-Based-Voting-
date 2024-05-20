pragma solidity ^0.5.0;

contract Voting {
    struct Vote {
        uint256 voterId;
        string candidateName;
        uint256 blockNumber; // Add block number to the vote struct
    }

    mapping(uint256 => Vote) public votes;

    function vote(uint256 _voterId, string memory _candidateName) public {
        uint256 currentBlockNumber = block.number; // Get the current block number
        votes[_voterId] = Vote(_voterId, _candidateName, currentBlockNumber);
    }

    function getVote(uint256 _voterId) public view returns (uint256, string memory, uint256) {
        Vote memory voteData = votes[_voterId];
        return (voteData.voterId, voteData.candidateName, voteData.blockNumber);
    }

    mapping(address => bool) public voters;
    mapping(string => uint256) private votesReceived;
    uint256 public taskCount;

    event VoteCast(address indexed voter, string candidate);
    event TaskCreated(address indexed creator);

    constructor() public {
        taskCount = 0; // Initialize task count to 0
    }

    function vote(string memory candidate) public {
        require(!voters[msg.sender], "You have already voted.");
        voters[msg.sender] = true;
        votesReceived[candidate]++;
        emit VoteCast(msg.sender, candidate);
    }

    function getVotesForCandidate(string memory candidate) public view returns (uint256) {
        return votesReceived[candidate];
    }

    function createTask() public {
        taskCount++;
        emit TaskCreated(msg.sender);
    }

    function getTaskCount() public view returns (uint256) {
        return taskCount;
    }
}
