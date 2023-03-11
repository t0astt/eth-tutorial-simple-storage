from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange,
    account = accounts[0]

    # act,
    ss = SimpleStorage.deploy({"from": account})
    starting_value = ss.retrieve()
    expected = 0
    # assert
    assert starting_value == expected

def test_updating_storage():
    # arrange
    account = accounts[0]
    ss = SimpleStorage.deploy({"from": account})
    # act
    expected = 15
    ss.store(expected, {"from": account})
    # assert
    assert expected == ss.retrieve()
