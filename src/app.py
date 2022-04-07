import os
import binascii
from web3.auto import w3

WALLET_PATH = os.environ['WALLET_PATH']
WALLET_PWD = os.environ['WALLET_PWD']

with open(os.path.join(WALLET_PATH, 'wallet.json')) as json_keyfile:
    encrypted_key = json_keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, WALLET_PWD)
    with open(os.path.join(WALLET_PATH, 'private_key.txt'), 'w+') as hex_keyfile:
        hex_keyfile.write(str(binascii.b2a_hex(private_key)))
