<h1> BlockChain Based Voting System </h1>
This project aims to create a secure voting system which stores each vote as a block with a hash code generated and each vote creates a new transcation. The Votes block details can be viewed in the Ganache framework.
The Etereum account can be choosen from the Ganache framework as it simulates a Ethereum Wallet.

<h1>Required framewoek:</h1>
-Download node.js<br>
-Download Ganache (Truffle will be done in terminal in your project directorty)<br>
-Remix IDE (Google)<br>

<h1>Steps to start with the project:</h1>
1. Create a folder with any name of choice and open that in VS code.<br>
2. Once youre in the directory add these files: app.py, create a folder and name it "templates" and under that add: index.html, thank_you.html, block_details.html.<br>
3. Now open terminal and move into your project directory and type in the following commands to download truffle and interact with the gancache framework: <br>
       - npm -v (to check if npm is installed)<br>
       - npm install truffle<br>
       - npm init (Initialize truffle, this will few folders (Contract, migration, test) and a truffle-config.js in your directory in VS code.<br>
4. Now you will need to modify the the truffle-config.js file, open the file and go network and uncomment the documents and then scroll down to solc and uncomment optimizer ONLY.<br>
5. Now add the .sol files to the Contracts folder. <br>
6. Add the migrations file to the migration folder and change the variable name to whatever you have named the .sol file. <br>
7. Open Remix IDE and create a .sol file there and compile. After compiling you will see at abi copy button just copy that and create a file in the main directory of your folder named "yourfile.abi" <br>
8. Below the compile button on remix there should be a deploy button, open that and deploy the file, in terminal you should see a down arrow click on that and scroll till contract address, copy this adress and paste it in the app.py where contract_address is located.<br>
9. The from_address in your app.py is from the ganache account. Copy the address of any account and paste it.<br>
10. After you have made all these changes go to terminal and type these commands : <br>
        - truffle compile<br>
        - truffle migrate<br>
11. migrate will interact with the contract address and the account and Transaction will be created.<br>
