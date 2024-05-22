import web3

def swap(to_symbol):
    """Swap ETH for another token."""

    # Get the contract ABI and address.
    abi = json.load(open("uniswap_router_abi.json"))
    contract_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"

    # Create the contract object.
    contract = web3.eth.contract(address=contract_address, abi=abi)

    # Get the amount of ETH to swap.
    eth_amount = web3.toWei(1, "ether")

    # Get the amount of tokens to receive.
    amount_out = contract.functions.getAmountsOut(eth_amount, [web3.toChecksumAddress("0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")]).call()[-1]

    # Approve the swap.
    approve_tx_hash = contract.functions.approve(contract_address, eth_amount).transact()
    web3.eth.wait_for_transaction_receipt(approve_tx_hash)

    # Swap the tokens.
    swap_tx_hash = contract.functions.swapExactETHForTokens(0, amount_out, [web3.toChecksumAddress("0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")], web3.toChecksumAddress(accounts[0])).transact({'value': eth_amount})
    web3.eth.wait_for_transaction_receipt(swap_tx_hash)

    # Print the transaction hash.
    print(f'\n>>> swap {to_symbol} | https://www.example.com 'green')
