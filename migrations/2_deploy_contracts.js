// 2_deploy_contracts.js
const Voting = artifacts.require('Voting');

module.exports = function(deployer) {
  deployer.deploy(Voting);
};

 // Assuming you have already deployed your contract and have the contract address
//const Voting = artifacts.require('Voting'); // Import your contract artifact

module.exports = async function (deployer) {
    // Deploy your contract if needed
    await deployer.deploy(Voting);

    // Get an instance of the deployed contract
    const votingInstance = await Voting.deployed();
   

    // Now you can interact with the contract using votingInstance
    // For example, calling a function:
    const result = await votingInstance.getVote(2);
    console.log(result);
};
