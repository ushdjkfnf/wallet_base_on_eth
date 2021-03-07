import json
from web3 import Web3, HTTPProvider
import sys

key_file_name = input("key file name: ")

from_address = input("from_address: ")
to_address = input("to_address: ")
# to_address = "0x1f0ea83ea17c6abc504b8c9513574dc6b638f212"

print("confirm receiver again! {}".format(to_address))

answer = input("ok: ")
if answer == "yes":
    pass
else:
    print("abort")
    sys.exit(1)

amount = input("amount: ")
amount = int(amount + '000000')
password=input("password")

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
},
{
  "constant": false,
  "inputs": [{
    "name": "",
    "type": "address"
  }, {
    "name": "",
    "type": "uint256"
  }],
  "name": "transfer",
  "outputs": [],
  "payable": true,
  "type": "function"
  }]
'''

w3 = Web3(HTTPProvider('http://localhost:8545') )

# source_code = w3.eth.getCode(usdt_contract_address)

abi = json.loads(contract_source_code)


contract = w3.eth.contract(abi=abi, address=usdt_contract_address)

# 1usdt=1 000 000
# gasPrice 43000000000
usdt_txn = contract.functions.transfer(
my2,
amount,
).buildTransaction({
'chainId': 1,
'gas': 60000,
'gasPrice': w3.eth.gasPrice,
# 'gasPrice': 100000000000,
'nonce': w3.eth.getTransactionCount(my),
})

print(usdt_txn)


with open('/data/geth/keystore/{}'.format(key_file_name)) as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, password)

signed_txn = w3.eth.account.sign_transaction(usdt_txn, private_key)

ret = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

print(ret)
print(ret.decode())
