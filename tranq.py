import multiprocessing
import utils.csv.core
import utils.web3.core


def fetch_transaction_method(hash):
    detailed_transaction = utils.web3.core.client.eth.get_transaction(hash)
    return detailed_transaction.input[0:10]


def fetch_deposited_tranq(start_block, end_block):
    def process_event(event, addresses):
        method = fetch_transaction_method(event.transactionHash.hex())
        if (method == '0xb6b55f25'):
            # Deposit.
            amount = event.args.amount / 1e18
            address = event.args['from']

            if(address not in addresses):
                addresses[address] = 0

            addresses[address] += amount

    return utils.web3.core.fetch_transfer_events(
        utils.web3.core.tranq_token,
        {'to': utils.web3.core.address_tranq_locked_staking},
        start_block,
        end_block,
        process_event
    )


def fetch_withdrawn_tranq(start_block, end_block):
    def process_event(event, addresses):
        method = fetch_transaction_method(event.transactionHash.hex())

        if(method == '0xdb006a75'):
            # Regular redeem.
            amount = event.args.amount / 1e18
            address = event.args['to']

            if(address not in addresses):
                addresses[address] = 0

            addresses[address] += amount
        elif(method == '0x2706cab4'):
            # Early redeem.
            amount = event.args.amount / 1e18
            address = event.args['to']

            if(address not in addresses):
                addresses[address] = 0

            addresses[address] += amount * 2

    return utils.web3.core.fetch_transfer_events(
        utils.web3.core.tranq_token,
        {'from': utils.web3.core.address_tranq_locked_staking},
        start_block,
        end_block,
        process_event
    )


def add_all(snapshot, balances):
    for balance in balances:
        for address, amount in balance.items():
            snapshot[address] = snapshot.get(address, 0) + amount


def subtract_all(snapshot, balances):
    for balance in balances:
        for address, amount in balance.items():
            snapshot[address] = snapshot.get(address, 0) - amount


def output_to_csv(writer, addresses):
    writer.writerow(['address', 'amount'])

    for address, amount in addresses.items():
        writer.writerow([address, round(amount, 4)])


if __name__ == '__main__':
    # Gen0 round 1 mint end block = 26472660 https://explorer.harmony.one/tx/0x31d9575f169d05937af3b7d4f6c7a5bf6ef673b6716dc9eee2f2f71ed8e0dbb8

    # Initialize variables.
    parameters = utils.web3.core.get_block_tuples(19000000, 26472660)

    # Execute function in parallel.
    pool = multiprocessing.Pool()
    deposited_tranq_balances = pool.starmap(fetch_deposited_tranq, parameters)
    withdrawn_tranq_balances = pool.starmap(fetch_withdrawn_tranq, parameters)
    pool.close()
    pool.join()

    # Merge function results.
    snapshot = {}
    add_all(snapshot, deposited_tranq_balances)
    subtract_all(snapshot, withdrawn_tranq_balances)

    # Write the snapshot to CSV.
    utils.csv.core.write(
        f'tranq-holders',
        lambda writer: output_to_csv(writer, snapshot)
    )
