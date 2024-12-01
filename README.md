# FetchBitcoinAddress
I've added a brief explanation at the beginning of the README. Let me know if you need any further modifications or additional information.


BIP44 Address Search Tool

This repository contains a Python script for deriving and searching Bitcoin addresses based on different BIP standards. It is useful for users who want to retrieve keys or validate addresses derived from a specific seed phrase.

This Python script searches for Bitcoin addresses derived from a provided seed phrase using BIP44, BIP49, and BIP84 standards. The script allows you to extract the private and public keys for Legacy (P2PKH), Nested SegWit (P2SH), and Native SegWit (P2WPKH) Bitcoin addresses. It iterates through a specified number of derived addresses to find a match for a target address.

Features

Supports Legacy (P2PKH), Nested SegWit (P2SH), and Native SegWit (P2WPKH) addresses.

Extracts private keys, public keys, and associated addresses.

Can be used to match against a target address.

Requirements

Python 3.x

bip-utils library

Install the required library using pip:

pip install bip-utils

Usage

Clone this repository or copy the script.

Update the following variables in the script:

mnemonic: The seed phrase used to generate the keys and addresses.

target_address: The Bitcoin address you want to match against.

addr_limit: The number of addresses to search (default is 1000, but you can adjust this).

Run the script:

python bip44_address_search.py

The script will generate and display addresses, private keys, and public keys derived from the provided seed phrase. If a match is found with the target address, the corresponding keys will be displayed.

Example Output

Checking Legacy (P2PKH) addresses...
Address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa (Type: Legacy (P2PKH))
Private Key: <private_key_here>
Public Key: <public_key_here>
...

Match found!
Address: 14ar89XeApcrr2UktdF8BmMANdhvSnfADM
Private Key: <private_key_here>
Public Key: <public_key_here>

Notes

The seed phrase provided in the script is for demonstration purposes only. Use your own seed phrase for actual searches.

Be careful with your private key and seed phrase; anyone with access to these can control your funds.

Adjust addr_limit as needed to search more or fewer addresses.

License

This project is licensed under the MIT License.
