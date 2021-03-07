import json
from web3 import Web3, HTTPProvider

key_file_name = input("key file name: ")


password=input("password")

from_address = input("from_address: ")
to_address = input("to_address: ")


my = Web3.toChecksumAddress(from_address)

my2 = Web3.toChecksumAddress(to_address)



usdt_contract_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

contract_source_code='''
[{
  "type":"function",
  "name":"balanceOf",
  "constant":true,
  "payable":false,
  "inputs":[{"name":"","type":"address"}],
  "outputs":[{"name":"","type":"uint256","value":"0"}]
}]
'''
abi = json.loads(contract_source_code)

w3 = Web3(HTTPProvider('http://localhost:8545') )

source_code = w3.eth.getCode(usdt_contract_address)
contract = w3.eth.contract(abi=abi, address=usdt_contract_address)

with open('/data/geth/keystore/{}'.format(key_file_name)) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, password)

transaction = dict(
    nonce=w3.eth.getTransactionCount(my),
    gasPrice=w3.eth.gasPrice,
    gas=100000,
    to=my2,
    value=w3.toWei(0.04,'ether'),
    chainId=1
)
signed_txn = w3.eth.account.signTransaction(transaction, private_key)

w3.eth.sendRawTransaction(signed_txn.rawTransaction)