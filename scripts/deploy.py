from brownie import accounts, config, SimpleStorage, network
import dotenv

dotenv.load_dotenv(".env")


def deploy_simple_storage():
    account = get_account()
    ss = SimpleStorage.deploy({"from": account})
    transaction = ss.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = ss.retrieve()
    print(updated_stored_value)


def get_account():
    """
    Easy way for determining which account to test, local, testnet, prod, etc
    :return:
    """
    if network.show_active == "development":
        print("Deploying to development")
        return accounts[0]
    else:
        private_key = config["wallets"]["from_key"]
        print("Deploying to network")
        print(f"Got private key {private_key}")
        return accounts.add(private_key)


def main():
    deploy_simple_storage()