import os
from dotenv import load_dotenv
from xrpl.wallet import Wallet
from xrpl.utils import str_to_hex
from xrpl.models import Transaction
from xrpl.transaction import sign

load_dotenv()

seed = os.getenv("WALLET_SEED")
if seed is None:
    raise EnvironmentError("Environment variable WALLET_SEED not set")

wallet = Wallet.from_seed(seed)
address = wallet.address
print(f"Successfully loaded wallet: {address}")

message = os.getenv("MESSAGE")
if message is None:
    raise EnvironmentError("Environment variable MESSAGE not set")

print("Loading transaction data...")
hex_message = str_to_hex(message)
transaction_json = {
    "account": address,
    "transaction_type": "AccountSet",
    "memos": [
        {
            "memo": {
                "memo_data": hex_message
            }
        }
    ]
}

print("Signing the message...")
transaction = Transaction.from_dict(transaction_json)
signature = sign(transaction, wallet)

print(f"Successfully signed the message: {signature.txn_signature}")
print(f"Using following public key: {signature.signing_pub_key}")

