import sys
from web3 import Web3

RPC_URL = "https://mainnet.base.org"


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py 0xAdresseWallet")
        return

    wallet = sys.argv[1]
    web3 = Web3(Web3.HTTPProvider(RPC_URL))

    if not web3.is_address(wallet):
        print("Adresse invalide")
        return

    checksum_wallet = web3.to_checksum_address(wallet)
    balance_wei = web3.eth.get_balance(checksum_wallet)
    balance_eth = web3.from_wei(balance_wei, "ether")

    print("=== Base Wallet Stats ===")
    print(f"Wallet : {checksum_wallet}")
    print(f"Solde ETH : {balance_eth}")


if __name__ == "__main__":
    main()
