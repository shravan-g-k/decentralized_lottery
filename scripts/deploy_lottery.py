
from brownie import Lottery
from scripts.heplful_scripts import get_account


def  deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy()


def main():
    deploy_lottery()