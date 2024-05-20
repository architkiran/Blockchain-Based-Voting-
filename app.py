from flask import Flask, render_template, request, redirect, url_for
from web3 import Web3
from datetime import datetime
import json
import sqlite3

app = Flask(__name__)

# Initialize Web3 instance
web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))  # Connect to local Ganache instance

# Load smart contract ABI from file
with open('Voting.abi', 'r') as f:
    contract_abi = json.load(f)

# Address of deployed smart contract
contract_address = '0xd9145CCE52D386f254917e481eB44e9943F39138'  # Replace with your actual contract address

# Account address that will be used to send transactions
from_address = '0xdd14d7F3D4A6f2B7b671194464c7379681D2f73b'  # Replace with your actual Ethereum address

# Initialize smart contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
current_block_number = 100 

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_block_number
    if request.method == 'POST':
        selected_candidate = request.form['candidate']
        selected_voter_id = request.form['voter_id']
        
        # Call smart contract function to record vote
        tx_hash = contract.functions.vote(selected_candidate).transact({'from': from_address})
        
        # Wait for transaction receipt
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        current_block_number += 1
        # Insert vote details into the SQLite database
        record_vote(selected_voter_id, selected_candidate)
        
        return redirect(url_for('thank_you', candidate=selected_candidate, voter_id=selected_voter_id))
    else:
        # Render candidate list from smart contract data
        candidates = ["Candidate A", "Candidate B", "Candidate C"]  # Replace with actual candidate list
        return render_template('index.html', candidates=candidates)

def record_vote(voter_id, candidate):
    try:
        # Connect to the database
        conn = sqlite3.connect('votes.db')
        print("Connected to SQLite database")

        # Create a cursor object
        c = conn.cursor()

        # Execute the INSERT statement
        c.execute('''INSERT INTO votes (voter_id, candidate) VALUES (?, ?)''', (voter_id, candidate))

        # Commit the changes
        conn.commit()
        print("Vote recorded successfully")

    except sqlite3.Error as e:
        print("SQLite error:", e)

    finally:
        # Close the connection
        conn.close()


@app.route('/thank-you')
def thank_you():
    selected_candidate = request.args.get('candidate', 'Unknown')
    voter_id = request.args.get('voter_id', 'Unknown')
    return render_template('thank_you.html', selected_candidate=selected_candidate, voter_id=voter_id)

@app.route('/block/<int:voter_id>')
def block_details(voter_id):
    # Retrieve block details based on voter ID from smart contract or blockchain
    # Example: block = contract.functions.getBlockByVoterId(voter_id).call()
    global current_block_number
    block = {
        'number': current_block_number,  # Example block number
        'hash': '0xabcdef123456...',  # Example block hash
        'timestamp': datetime.now(),  # Example timestamp
        'parentHash': '0x1234567890abcdef...'  # Example parent hash
        # Add more block details as needed
    }
    return render_template('block_details.html', block=block)


if __name__ == '__main__':
    app.run(debug=True)