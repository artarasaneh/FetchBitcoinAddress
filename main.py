# extract_native_segwit_keys.py
from bip_utils import Bip39SeedGenerator, Bip84, Bip84Coins, Bip84Changes

# Seed phrase provided by user
mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

# Target wallet address (to match against)
target_address = "bc1qar0srrr7xfkvy5l643c7vdhss0g5s2g7lmj6ljl3wllkudsl3tqcc"

# Generate seed from mnemonic
seed_bytes = Bip39SeedGenerator(mnemonic).Generate()

# Number of addresses to search
addr_limit = 1000  # Adjust this value as needed

print("\nChecking Native SegWit (P2WPKH) addresses...")

# Create BIP84 wallet based on the relevant derivation path
bip_mst = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN).Account(0)

# Iterate through derivation paths for receiving (Change(0)) and change (Change(1)) addresses
for change_type in [Bip84Changes.CHAIN_EXT, Bip84Changes.CHAIN_INT]:
    for addr_index in range(0, addr_limit):  # Search through the first 1000 addresses
        bip_acc = bip_mst.Change(change_type).AddressIndex(addr_index)

        # Extract private key
        private_key = bip_acc.PrivateKey().Raw().ToHex()

        # Extract public key
        public_key = bip_acc.PublicKey().RawCompressed().ToHex()

        # Generate address from public key
        generated_address = bip_acc.PublicKey().ToAddress()

        # Print keys and address (for verification)
        print(f"Address: {generated_address} (Native SegWit)")
        print(f"Private Key: {private_key}")
        print(f"Public Key: {public_key}")

        # Match against target address
        if generated_address == target_address:
            print("\nMatch found!")
            print(f"Address: {generated_address}")
            print(f"Private Key: {private_key}")
            print(f"Public Key: {public_key}")
            exit(0)

print("\nNo matching address found in the searched range.")
