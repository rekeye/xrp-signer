import os
import getpass
from xrpl.wallet import Wallet
from xrpl.utils import str_to_hex
from xrpl.models import AccountSet, Memo
from xrpl.transaction import sign, autofill_and_sign
from xrpl.clients import JsonRpcClient

seed = getpass.getpass("What's your signer wallet seed? ")

wallet = Wallet.from_seed(seed)
address = wallet.address
print(f"Successfully loaded wallet: {address}")

message = input("What message do you want signed? ")

print("Loading transaction data...")
hex_message = str_to_hex(message)
transaction = AccountSet(
    account=address,
    memos=[
        Memo(
            memo_data=hex_message
        ),
    ],
)

print("Signing the message...")
signature = sign(transaction, wallet)

print(f"Successfully signed the message: {signature.txn_signature}")
print(f"Using following public key: {signature.signing_pub_key}")

