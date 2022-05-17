# Defira genesis hero mint round 4.5 whitelist generator

## Context

Some users were not able to mint a hero during round 1 of Defira's genesis hero minting event due to a frontend UI bug where the “Mint” button would only be enabled if the wallet had more than 0 FIRA (not staked).

To give another opportunity to the affected users, the team will hold another round after round 4 - round 4.5 - with 100 genesis heroes and with the same 50,000 locked TRANQ requirement and 0 FIRA cost.

In order to determine which users were affected by this bug and are thus eligible to participate in round 4.5, a snapshot has to be built which represents the exact situation for each round 1 eligible wallet at the time of mint.

The snapshot is built by processing all transactions related to TRANQ transfers to and from the locked TRANQ staking contract, as well as processing all transactions related to FIRA transfers between wallets and contracts.

All transactions up until block 26472660 are processed, in which the last Gen0 hero of round 1 was sold and thus ending the round. If a wallet had >= 50,000 locked TRANQ and 0 FIRA at this block, then it is whitelisted for round 4.5.

## Requirements to run the script

* [Python 3+](https://www.python.org/)
* [web3](https://web3py.readthedocs.io/en/stable/)

## Running the script

1. Run `py tranq.py`
    * Generates `output/tranq-holders.csv` which is needed for the second part of the script
1. Run `py fira.py`
    * Generates `output/tranq-holders-with-fira-balances-eligible-for-round-1` which represents the whitelist for round 4.5 (each address having exactly 0 FIRA is whitelisted)