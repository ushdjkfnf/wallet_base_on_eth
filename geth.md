### geth.md

- set up a light node
```
data_dir="/data/geth"

/usr/local/bin/geth --syncmode "light" --datadir $data_dir --cache 2048 --txpool.globalslots 65535 --maxpeers 1000 --http --http.api "eth,net,web3,admin,personal,txpool" --http.corsdomain "*" --allow-insecure-unlock

```


- learn more details

```
https://geth.ethereum.org/docs/install-and-build/installing-geth
https://ethereum.org/en/developers/tutorials/run-light-node-geth/
https://geth.ethereum.org/docs/interface/managing-your-accounts
```

- make your own account

```
geth attach ${data_dir}/geth.ipc
personal.newAccount()

```