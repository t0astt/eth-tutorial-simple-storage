from brownie import SimpleStorage, accounts, config


def read_contract():
    # acts like an array
    ss = SimpleStorage[-1]  # take index one less than length for latest
    # ABI
    # Address
    print(ss.retrieve())

def main():
    read_contract()