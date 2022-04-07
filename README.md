# utc-key-converter
⚠️ NEVER SHARE YOUR PRIVATE KEYS EVER⚠️

Python [web3](https://web3py.readthedocs.io/en/stable/#) based utility to convert UTC wallet private key files to a hex string representation.

#### input
- The wallet.json keystore path
- The wallet.json's password

The keystore file should look like: 

    {
    "address": "ac21XXede9a8fc88097XXa4b02d15a823e6XX4c2",    
    "id": "8edXX4ad-XXf0-4be4-XXa6-bXXd16e04f08",
    "version": 3,
    "Crypto": { ...}  }

#### output
- The converted private key (private_key.txt), ex : `b'45ee5XXe181XX0c43f76XX06cb7f56781f9843f0bf1XX31b79fa7adXX6815bXX'` 

####  Usage

##### build

    docker build . --tag utc-key-converter

##### run
    docker run --rm -v ${PWD}:/WALLET_PATH -e WALLET_PATH=/WALLET_PATH/ -e WALLET_PWD="1" utc-key-converter:latest

  
