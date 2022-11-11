from brownie import Lottery
from scripts.heplful_scripts import get_account, get_contract


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth-usd-prce-feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,


    )


def main():
    deploy_lottery()
