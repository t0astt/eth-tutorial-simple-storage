deploy-local:
	brownie run scripts/deploy.py

deploy-goerli:
	brownie run scripts/deploy.py --network goerli

deploy-sepolia:
	brownie run scripts/deploy.py --network sepolia

test:
	brownie test -s

networks_list:
	brownie networks list True