from web3 import Web3
import time

# Replace with your Metamask wallet private key and RPC URL
PRIVATE_KEY = "your_private_key"
RPC_URL = "your_rpc_url"
REFERRAL_ADDRESS = "your_referral_address"

# Connect to blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))
if web3.isConnected():
    print("Connected to the blockchain!")
else:
    raise Exception("Failed to connect to blockchain.")

# Wallet address and account
account = web3.eth.account.from_key(PRIVATE_KEY)
wallet_address = account.address
print(f"Wallet Address: {wallet_address}")

# Function to claim daily reward
def claim_reward():
    print("Claiming daily reward...")
    # Example: Replace with the actual contract and method to call
    contract_address = "contract_address_here"
    contract_abi = "contract_abi_here"
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Claim reward function call
    tx = contract.functions.claimDailyReward(REFERRAL_ADDRESS).buildTransaction({
        'from': wallet_address,
        'nonce': web3.eth.getTransactionCount(wallet_address),
        'gas': 200000,
        'gasPrice': web3.toWei('50', 'gwei')
    })

    # Sign and send the transaction
    signed_tx = web3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction sent! Hash: {tx_hash.hex()}")

    # Wait for confirmation
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Transaction confirmed! Block: {receipt.blockNumber}")

# Main loop
while True:
    try:
        claim_reward()
        print("Reward claimed. Switching account...")

        # Logic to switch account (add your own implementation)
        time.sleep(86400)  # Wait for 24 hours
    except Exception as e:
        print(f"Error: {e}")