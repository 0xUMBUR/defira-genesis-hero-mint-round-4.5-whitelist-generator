abi = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "payable": False,
        "type": "constructor",
        "stateMutability": "nonpayable"
    },
    {
        "name": "Approval",
        "type": "event",
        "anonymous": False,
        "inputs": [
            {
                "type": "address",
                "indexed": True,
                "name": "owner",
                "internalType": "address"
            },
            {
                "name": "spender",
                "type": "address",
                "indexed": True,
                "internalType": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ]
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "delegator",
                "indexed": True,
                "type": "address"
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
        "type": "event",
        "name": "DelegateChanged"
    },
    {
        "anonymous": False,
        "name": "DelegateVotesChanged",
        "inputs": [
            {
                "type": "address",
                "name": "delegate",
                "internalType": "address",
                "indexed": True
            },
            {
                "indexed": False,
                "type": "uint256",
                "internalType": "uint256",
                "name": "previousBalance"
            },
            {
                "internalType": "uint256",
                "indexed": False,
                "name": "newBalance",
                "type": "uint256"
            }
        ],
        "type": "event"
    },
    {
        "type": "event",
        "anonymous": False,
        "name": "Transfer",
        "inputs": [
            {
                "indexed": True,
                "name": "from",
                "internalType": "address",
                "type": "address"
            },
            {
                "internalType": "address",
                "indexed": True,
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256",
                "indexed": False
            }
        ]
    },
    {
        "constant": True,
        "outputs": [
            {
                "type": "bytes32",
                "internalType": "bytes32",
                "name": ""
            }
        ],
        "type": "function",
        "inputs": [],
        "name": "DELEGATION_TYPEHASH",
        "stateMutability": "view",
        "payable": False
    },
    {
        "constant": True,
        "name": "DOMAIN_TYPEHASH",
        "payable": False,
        "outputs": [
            {
                "name": "",
                "type": "bytes32",
                "internalType": "bytes32"
            }
        ],
        "type": "function",
        "inputs": [],
        "stateMutability": "view"
    },
    {
        "name": "PERMIT_TYPEHASH",
        "stateMutability": "view",
        "payable": False,
        "outputs": [
            {
                "type": "bytes32",
                "name": "",
                "internalType": "bytes32"
            }
        ],
        "constant": True,
        "type": "function",
        "inputs": []
    },
    {
        "type": "function",
        "payable": False,
        "stateMutability": "view",
        "constant": True,
        "name": "checkpoints",
        "inputs": [
            {
                "type": "address",
                "name": "",
                "internalType": "address"
            },
            {
                "type": "uint32",
                "internalType": "uint32",
                "name": ""
            }
        ],
        "outputs": [
            {
                "type": "uint32",
                "name": "fromBlock",
                "internalType": "uint32"
            },
            {
                "name": "votes",
                "type": "uint96",
                "internalType": "uint96"
            }
        ]
    },
    {
        "name": "decimals",
        "payable": False,
        "constant": True,
        "stateMutability": "view",
        "inputs": [],
        "outputs": [
            {
                "internalType": "uint8",
                "type": "uint8",
                "name": ""
            }
        ],
        "type": "function"
    },
    {
        "name": "delegates",
        "type": "function",
        "stateMutability": "view",
        "outputs": [
            {
                "name": "",
                "type": "address",
                "internalType": "address"
            }
        ],
        "constant": True,
        "inputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False
    },
    {
        "name": "name",
        "inputs": [],
        "type": "function",
        "stateMutability": "view",
        "payable": False,
        "constant": True,
        "outputs": [
            {
                "type": "string",
                "internalType": "string",
                "name": ""
            }
        ]
    },
    {
        "name": "nonces",
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "constant": True,
        "payable": False,
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": ""
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "name": "numCheckpoints",
        "outputs": [
            {
                "type": "uint32",
                "internalType": "uint32",
                "name": ""
            }
        ],
        "type": "function",
        "payable": False,
        "inputs": [
            {
                "name": "",
                "internalType": "address",
                "type": "address"
            }
        ],
        "constant": True,
        "stateMutability": "view"
    },
    {
        "outputs": [
            {
                "type": "string",
                "name": "",
                "internalType": "string"
            }
        ],
        "payable": False,
        "inputs": [],
        "type": "function",
        "stateMutability": "view",
        "name": "symbol",
        "constant": True
    },
    {
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256",
                "internalType": "uint256"
            }
        ],
        "payable": False,
        "type": "function",
        "inputs": [],
        "constant": True,
        "stateMutability": "view"
    },
    {
        "payable": False,
        "type": "function",
        "name": "allowance",
        "constant": True,
        "inputs": [
            {
                "type": "address",
                "internalType": "address",
                "name": "account"
            },
            {
                "name": "spender",
                "internalType": "address",
                "type": "address"
            }
        ],
        "stateMutability": "view",
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
        "outputs": [
            {
                "type": "bool",
                "internalType": "bool",
                "name": ""
            }
        ],
        "inputs": [
            {
                "type": "address",
                "name": "spender",
                "internalType": "address"
            },
            {
                "name": "rawAmount",
                "internalType": "uint256",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "payable": False,
        "constant": False,
        "stateMutability": "nonpayable"
    },
    {
        "type": "function",
        "name": "permit",
        "constant": False,
        "outputs": [],
        "payable": False,
        "inputs": [
            {
                "name": "owner",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "address",
                "name": "spender",
                "internalType": "address"
            },
            {
                "name": "rawAmount",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "deadline",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "internalType": "uint8",
                "type": "uint8",
                "name": "v"
            },
            {
                "internalType": "bytes32",
                "type": "bytes32",
                "name": "r"
            },
            {
                "internalType": "bytes32",
                "type": "bytes32",
                "name": "s"
            }
        ],
        "stateMutability": "nonpayable"
    },
    {
        "payable": False,
        "name": "balanceOf",
        "constant": True,
        "type": "function",
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
                "name": "account",
                "internalType": "address",
                "type": "address"
            }
        ]
    },
    {
        "name": "transfer",
        "payable": False,
        "inputs": [
            {
                "type": "address",
                "name": "dst",
                "internalType": "address"
            },
            {
                "type": "uint256",
                "name": "rawAmount",
                "internalType": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "outputs": [
            {
                "name": "",
                "internalType": "bool",
                "type": "bool"
            }
        ],
        "constant": False,
        "type": "function"
    },
    {
        "inputs": [
            {
                "name": "src",
                "internalType": "address",
                "type": "address"
            },
            {
                "type": "address",
                "name": "dst",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "type": "uint256",
                "name": "rawAmount"
            }
        ],
        "type": "function",
        "outputs": [
            {
                "name": "",
                "internalType": "bool",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "name": "transferFrom",
        "payable": False,
        "constant": False
    },
    {
        "payable": False,
        "name": "delegate",
        "outputs": [],
        "constant": False,
        "stateMutability": "nonpayable",
        "inputs": [
            {
                "internalType": "address",
                "type": "address",
                "name": "delegatee"
            }
        ],
        "type": "function"
    },
    {
        "type": "function",
        "constant": False,
        "outputs": [],
        "inputs": [
            {
                "name": "delegatee",
                "type": "address",
                "internalType": "address"
            },
            {
                "name": "nonce",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "expiry",
                "type": "uint256",
                "internalType": "uint256"
            },
            {
                "name": "v",
                "type": "uint8",
                "internalType": "uint8"
            },
            {
                "name": "r",
                "type": "bytes32",
                "internalType": "bytes32"
            },
            {
                "name": "s",
                "type": "bytes32",
                "internalType": "bytes32"
            }
        ],
        "stateMutability": "nonpayable",
        "payable": False,
        "name": "delegateBySig"
    },
    {
        "outputs": [
            {
                "internalType": "uint96",
                "type": "uint96",
                "name": ""
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True,
        "payable": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
        ],
        "name": "getCurrentVotes"
    },
    {
        "payable": False,
        "type": "function",
        "outputs": [
            {
                "internalType": "uint96",
                "type": "uint96",
                "name": ""
            }
        ],
        "inputs": [
            {
                "type": "address",
                "name": "account",
                "internalType": "address"
            },
            {
                "internalType": "uint256",
                "name": "blockNumber",
                "type": "uint256"
            }
        ],
        "name": "getPriorVotes",
        "constant": True,
        "stateMutability": "view"
    }
]
