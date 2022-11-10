from brownie import config, network, accounts

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKACHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_VALUE = 20000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKACHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    
    return accounts.add(config["wallets"]["key"])
