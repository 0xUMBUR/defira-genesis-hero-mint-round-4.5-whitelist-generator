abi = [
    {
        "type": "constructor",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "type": "uint256",
                "name": "cap_",
                "internalType": "uint256"
            },
            {
                "name": "amount_",
                "internalType": "uint256",
                "type": "uint256"
            }
        ]
    },
    {
        "type": "event",
        "name": "Approval",
        "anonymous": False,
        "inputs": [
            {
                "name": "owner",
                "indexed": True,
                "type": "address",
                "internalType": "address"
            },
            {
                "internalType": "address",
                "indexed": True,
                "type": "address",
                "name": "spender"
            },
            {
                "indexed": False,
                "name": "value",
                "internalType": "uint256",
                "type": "uint256"
            }
        ]
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "delegator",
                "type": "address",
                "internalType": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "fromDelegate",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "toDelegate",
                "type": "address",
                "internalType": "address"
            }
        ],
        "name": "DelegateChanged",
        "type": "event"
    },
    {
        "inputs": [
            {
                "name": "delegate",
                "type": "address",
                "internalType": "address",
                "indexed": True
            },
            {
                "name": "previousBalance",
                "indexed": False,
                "internalType": "uint256",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "newBalance",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "anonymous": False,
        "name": "DelegateVotesChanged",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "type": "uint256",
                "indexed": False,
                "name": "previousRate",
                "internalType": "uint256"
            },
            {
                "type": "uint256",
                "indexed": False,
                "name": "newRate",
                "internalType": "uint256"
            }
        ],
        "type": "event",
        "name": "MaxTransferAmountRateUpdated"
    },
    {
        "name": "OwnershipTransferred",
        "anonymous": False,
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "previousOwner",
                "indexed": True
            },
            {
                "name": "newOwner",
                "internalType": "address",
                "indexed": True,
                "type": "address"
            }
        ],
        "type": "event"
    },
    {
        "type": "event",
        "inputs": [
            {
                "type": "address",
                "indexed": True,
                "internalType": "address",
                "name": "from"
            },
            {
                "name": "to",
                "internalType": "address",
                "indexed": True,
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256",
                "indexed": False
            }
        ],
        "anonymous": False,
        "name": "Transfer"
    },
    {
        "type": "function",
        "stateMutability": "view",
        "name": "DELEGATION_TYPEHASH",
        "inputs": [],
        "outputs": [
            {
                "type": "bytes32",
                "name": "",
                "internalType": "bytes32"
            }
        ],
        "constant": True,
        "signature": "0xe7a324dc"
    },
    {
        "stateMutability": "view",
        "inputs": [],
        "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
        ],
        "type": "function",
        "name": "DOMAIN_TYPEHASH",
        "constant": True,
        "signature": "0x20606b70"
    },
    {
        "inputs": [
            {
                "name": "_toAdd",
                "type": "address",
                "internalType": "address"
            }
        ],
        "type": "function",
        "stateMutability": "nonpayable",
        "name": "addAuthorized",
        "outputs": []
    },
    {
        "name": "allowance",
        "stateMutability": "view",
        "type": "function",
        "inputs": [
            {
                "type": "address",
                "name": "owner",
                "internalType": "address"
            },
            {
                "name": "spender",
                "type": "address",
                "internalType": "address"
            }
        ],
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ]
    },
    {
        "type": "function",
        "inputs": [
            {
                "name": "spender",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "amount",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "stateMutability": "nonpayable",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ]
    },
    {
        "name": "authorized",
        "type": "function",
        "stateMutability": "view",
        "inputs": [
            {
                "name": "",
                "internalType": "address",
                "type": "address"
            }
        ],
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ]
    },
    {
        "stateMutability": "view",
        "inputs": [
            {
                "name": "account",
                "internalType": "address",
                "type": "address"
            }
        ],
        "type": "function",
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "name": "balanceOf"
    },
    {
        "stateMutability": "nonpayable",
        "name": "burn",
        "inputs": [
            {
                "type": "uint256",
                "name": "amount",
                "internalType": "uint256"
            }
        ],
        "outputs": [],
        "type": "function"
    },
    {
        "outputs": [],
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "name": "account",
                "internalType": "address",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "burnFrom",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": ""
            },
            {
                "type": "uint32",
                "internalType": "uint32",
                "name": ""
            }
        ],
        "stateMutability": "view",
        "outputs": [
            {
                "name": "fromBlock",
                "internalType": "uint32",
                "type": "uint32"
            },
            {
                "name": "votes",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "type": "function",
        "name": "checkpoints"
    },
    {
        "stateMutability": "view",
        "name": "decimals",
        "type": "function",
        "inputs": [],
        "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "constant": True,
        "signature": "0x313ce567"
    },
    {
        "name": "decreaseAllowance",
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "name": "subtractedValue",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "type": "bool",
                "internalType": "bool",
                "name": ""
            }
        ],
        "type": "function",
        "stateMutability": "nonpayable"
    },
    {
        "outputs": [
            {
                "type": "bool",
                "internalType": "bool",
                "name": ""
            }
        ],
        "type": "function",
        "inputs": [
            {
                "type": "address",
                "name": "spender",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "name": "addedValue",
                "type": "uint256"
            }
        ],
        "name": "increaseAllowance",
        "stateMutability": "nonpayable"
    },
    {
        "inputs": [],
        "outputs": [
            {
                "type": "uint16",
                "name": "",
                "internalType": "uint16"
            }
        ],
        "name": "maxTransferAmountRate",
        "type": "function",
        "stateMutability": "view",
        "constant": True,
        "signature": "0x3ff8bf2e"
    },
    {
        "outputs": [
            {
                "name": "",
                "type": "string",
                "internalType": "string"
            }
        ],
        "inputs": [],
        "name": "name",
        "stateMutability": "view",
        "type": "function",
        "constant": True,
        "signature": "0x06fdde03"
    },
    {
        "outputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": ""
            }
        ],
        "stateMutability": "view",
        "inputs": [
            {
                "name": "",
                "internalType": "address",
                "type": "address"
            }
        ],
        "type": "function",
        "name": "nonces"
    },
    {
        "outputs": [
            {
                "type": "uint32",
                "internalType": "uint32",
                "name": ""
            }
        ],
        "type": "function",
        "stateMutability": "view",
        "name": "numCheckpoints",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": ""
            }
        ]
    },
    {
        "inputs": [],
        "stateMutability": "view",
        "name": "owner",
        "type": "function",
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "constant": True,
        "signature": "0x8da5cb5b"
    },
    {
        "outputs": [],
        "name": "removeAuthorized",
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": "_toRemove"
            }
        ]
    },
    {
        "inputs": [],
        "outputs": [],
        "stateMutability": "nonpayable",
        "name": "renounceOwnership",
        "type": "function"
    },
    {
        "stateMutability": "view",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "symbol",
        "inputs": [],
        "type": "function",
        "constant": True,
        "signature": "0x95d89b41"
    },
    {
        "name": "totalSupply",
        "stateMutability": "view",
        "outputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ],
        "type": "function",
        "inputs": [],
        "constant": True,
        "signature": "0x18160ddd"
    },
    {
        "stateMutability": "nonpayable",
        "name": "transfer",
        "type": "function",
        "inputs": [
            {
                "type": "address",
                "name": "recipient",
                "internalType": "address"
            },
            {
                "type": "uint256",
                "name": "amount",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "",
                "type": "bool",
                "internalType": "bool"
            }
        ]
    },
    {
        "type": "function",
        "inputs": [
            {
                "name": "sender",
                "type": "address",
                "internalType": "address"
            },
            {
                "type": "address",
                "name": "recipient",
                "internalType": "address"
            },
            {
                "name": "amount",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "",
                "type": "bool",
                "internalType": "bool"
            }
        ],
        "name": "transferFrom",
        "stateMutability": "nonpayable"
    },
    {
        "name": "transferOwnership",
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
        ],
        "outputs": []
    },
    {
        "name": "cap",
        "type": "function",
        "stateMutability": "view",
        "inputs": [],
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "constant": True,
        "signature": "0x355274ea"
    },
    {
        "stateMutability": "nonpayable",
        "name": "capUpdate",
        "type": "function",
        "inputs": [
            {
                "name": "_newCap",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": []
    },
    {
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [
            {
                "name": "_to",
                "type": "address",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "_amount"
            }
        ],
        "name": "mint"
    },
    {
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "name": "delegates",
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "delegator"
            }
        ]
    },
    {
        "name": "delegate",
        "type": "function",
        "stateMutability": "nonpayable",
        "outputs": [],
        "inputs": [
            {
                "name": "delegatee",
                "type": "address",
                "internalType": "address"
            }
        ]
    },
    {
        "name": "delegateBySig",
        "stateMutability": "nonpayable",
        "type": "function",
        "inputs": [
            {
                "name": "delegatee",
                "internalType": "address",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "expiry"
            },
            {
                "internalType": "uint8",
                "type": "uint8",
                "name": "v"
            },
            {
                "internalType": "bytes32",
                "name": "r",
                "type": "bytes32"
            },
            {
                "name": "s",
                "type": "bytes32",
                "internalType": "bytes32"
            }
        ],
        "outputs": []
    },
    {
        "name": "getCurrentVotes",
        "type": "function",
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "outputs": [
            {
                "type": "uint256",
                "name": "",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "view"
    },
    {
        "stateMutability": "view",
        "inputs": [
            {
                "name": "account",
                "internalType": "address",
                "type": "address"
            },
            {
                "name": "blockNumber",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "outputs": [
            {
                "name": "",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "type": "function",
        "name": "getPriorVotes"
    },
    {
        "inputs": [
            {
                "type": "uint16",
                "name": "_maxTransferAmountRate",
                "internalType": "uint16"
            }
        ],
        "stateMutability": "nonpayable",
        "name": "updateMaxTransferAmountRate",
        "outputs": [],
        "type": "function"
    },
    {
        "type": "function",
        "inputs": [],
        "stateMutability": "view",
        "outputs": [
            {
                "type": "uint256",
                "internalType": "uint256",
                "name": ""
            }
        ],
        "name": "maxTransferAmount",
        "constant": True,
        "signature": "0xa9e75723"
    },
    {
        "type": "function",
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": "_account"
            },
            {
                "name": "_excluded",
                "type": "bool",
                "internalType": "bool"
            }
        ],
        "outputs": [],
        "name": "setExcludedFromAntiWhale"
    }
]
