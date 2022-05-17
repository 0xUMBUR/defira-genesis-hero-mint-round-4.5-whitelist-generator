from web3 import Web3, HTTPProvider
import utils.web3.abi.tranq_token
import utils.web3.abi.fira_token


client = Web3(HTTPProvider('https://one.rpc.heavenswail.one'))
address_tranq_token = '0xCf1709Ad76A79d5a60210F23e81cE2460542A836'
address_fira_token = '0x2A719aF848bf365489E548BE5edbEC1D65858e59'
address_tranq_locked_staking = '0x55aE07Bb8Bae1501F9aEBF35801B5699eAE63bb7'

tranq_token = client.eth.contract(
    address=address_tranq_token,
    abi=utils.web3.abi.tranq_token.abi
)

fira_token = client.eth.contract(
    address=address_fira_token,
    abi=utils.web3.abi.fira_token.abi
)


def fetch_transfer_events(contract, filters, start_block, end_block, event_processor):
    addresses = {}

    filter = contract.events.Transfer.createFilter(
        fromBlock=start_block,
        toBlock=end_block,
        argument_filters=filters
    )

    events = filter.get_all_entries()

    for event in filter.get_all_entries():
        event_processor(event, addresses)

    print(f'Processed {len(events)} transactions from block {start_block} to {end_block}')

    return addresses


def get_block_tuples(start_block, end_block):
    iteration_block = start_block
    increments = 2000

    blocks = []

    while iteration_block < end_block:
        from_block = iteration_block
        to_block = iteration_block + increments

        if(to_block > end_block):
            to_block = end_block

        blocks.append((from_block, to_block))

        iteration_block += increments + 1

    return blocks
