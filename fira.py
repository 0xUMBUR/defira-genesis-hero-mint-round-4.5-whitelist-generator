import multiprocessing
import utils.csv.core
import utils.web3.core


def fetch_fira_balances(whitelisted_addresses, start_block, end_block):
    def process_event(event, addresses):
        from_address = event.args['from']
        to_address = event.args['to']
        amount = event.args['value'] / 1e18

        if(from_address in whitelisted_addresses):
            addresses[from_address] = addresses.get(from_address, 0) - amount

        if(to_address in whitelisted_addresses):
            addresses[to_address] = addresses.get(to_address, 0) + amount

    return utils.web3.core.fetch_transfer_events(
        utils.web3.core.fira_token,
        {},
        start_block,
        end_block,
        process_event
    )


def fetch_eligible_locked_tranq_holders():
    def convert_to_objects(reader):
        eligible_locked_tranq_holders = []

        next(reader)

        for row in reader:
            lockedTranq = float(row[1])

            if lockedTranq >= 50000:
                entry = {
                    'address': row[0],
                    'lockedTranq': lockedTranq
                }
                eligible_locked_tranq_holders.append(entry)

        return eligible_locked_tranq_holders

    return utils.csv.core.read('tranq-holders', convert_to_objects)


def extract_addresses_from_eligible_address_pool(pool):
    eligible_addresses = []

    for entry in pool:
        eligible_addresses.append(entry['address'])

    return eligible_addresses


def combine_parameters(eligible_addresses, blocks):
    parameters = []

    for block in blocks:
        parameters.append((eligible_addresses, *block))

    return parameters


def add_all(snapshot, balances):
    for balance in balances:
        for address, amount in balance.items():
            snapshot[address] = amount + snapshot.get(address, 0)


def output_to_csv(writer, addresses):
    writer.writerow(['address', 'locked tranq', 'fira in wallet'])

    for entry in addresses:
        address = entry['address']
        lockedTranq = entry['lockedTranq']
        firaInWallet = round(entry['fira'], 4)
        writer.writerow([address, lockedTranq, firaInWallet])


if __name__ == '__main__':
    # Gen0 round 1 mint end block = 26472660 https://explorer.harmony.one/tx/0x31d9575f169d05937af3b7d4f6c7a5bf6ef673b6716dc9eee2f2f71ed8e0dbb8

    # Initialize variables.
    address_pool = fetch_eligible_locked_tranq_holders()
    blocks = utils.web3.core.get_block_tuples(21000000, 26472660)
    eligible_addresses = extract_addresses_from_eligible_address_pool(address_pool)
    parameters = combine_parameters(eligible_addresses, blocks)

    # Execute function in parallel.
    pool = multiprocessing.Pool()
    fira_balances = pool.starmap(fetch_fira_balances, parameters)
    pool.close()
    pool.join()

    # Merge function results.
    snapshot = {}
    add_all(snapshot, fira_balances)

    # Add FIRA balances to the address pool.
    for entry in address_pool:
        address = entry['address']
        entry['fira'] = snapshot.get(address, 0)

    # Write the address pool contents to CSV.
    utils.csv.core.write(
        f'tranq-holders-with-fira-balances-eligible-for-round-1',
        lambda writer: output_to_csv(writer, address_pool)
    )
