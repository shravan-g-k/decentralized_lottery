from brownie import config, network, accounts, MockV3Aggregator, Contract,VRFCoordinatorMock

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKACHAIN_ENVIRONMENTS = ["development", "ganache-local"]
DECIMALS = 8
STARTING_VALUE = 20000000000


def get_account(index=None, id=None):
    if index:
        return accounts[0]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKACHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]

    return accounts.add(config["wallets"]["key"])


contract_to_mock = {
    "eth-usd-price-feed": MockV3Aggregator,
    "vrf-coordinator":VRFCoordinatorMock,
    # "link_token":

}


def get_contract(contract_name):
    """
    This func will get the contract address from brownie config if defined
    else will deploy a mock version of that contract
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKACHAIN_ENVIRONMENTS:
        if len(contract_type <= 0):
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]

        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks(decimals=DECIMALS, initial_value=STARTING_VALUE):
    account = get_account()
    mock_price_feed = MockV3Aggregator.deploy(
        decimals, initial_value, {"from": account}
    )
    print("Deployed")
