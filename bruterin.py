'''
Python script that generates random ethereum addresseses and checks
for an existing balance. Mathematically you are more likely to win the lottery every day
of your life than to ever find one but everyone enjoys a good treasure hunt
'''

from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import etherscan
import time
import asyncio
es = etherscan.Client(

    # Get an API key from Etherscan.io
    api_key='ENTER YOUR ETHERSCAN API KEY HERE',
    cache_expire_after=5,
    )


f = open('keys.txt', 'w')

###########################
# Checks if transactions have ocurred on the address
# @param address -> an Ethereum compatible hex address 0x...
# @return the transactions list object
###########################
def transaction_check(address):
    print(address)
    transactions = es.get_transactions_by_address(address)
    # Uncomment sleep or change the paramater to slow down or speed up API calls
    time.sleep(.21)
    return transactions

###########################
# Checks the balance of a given Ethereum address
# @param address -> an Ethereum comptaible hex address 0x...
# @return balance held in an address (if any)
###########################
def balance_check(address):
    bal = es.get_eth_balance(str(address))
    time.sleep(.021)
    return bal

           
while(True):
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    full_addr = '0x' + addr.hex()
    balance = balance_check(full_addr)
    
    # Currently interested in seeking accounts with a balance
    #transactions = transaction_check(full_addr)
    
    print(full_addr)
    if(balance != 0):
        print("FOUND")
        print(str(full_addr))
        print()
        print(str(private_key.hex()))
        f.write("Address: " + str(full_addr))
        f.write("\n")
        f.write("Priv: " + str(private_key.hex()))
        f.write("\n")
        
        # Optional break in the super unlikely event anything is ever found.
        #break
