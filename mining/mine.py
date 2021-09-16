from hashlib import sha256
import time

def generate_sha(code):
    """
    Function that returns the SHA encoded hash value

    Input parameters:
    -code: Alpha-numeric string that holds transaction information (str)

    Output:
    -hash: Valid SHA encoded hash value (str)

    """

    return sha256(code.encode('ascii')).hexdigest()

def Mine(block,transaction,hash_prev,zeros):
    """
    Function that returns the mining status

    Input parameters:
    -block: Block number (int)
    -transaction: Valid transaction (str)
    -hash_prev: The previous hash value hard coded (alpha-numeral)
    -zeros: Number of zeros to be included in the hash (int)

    Output:
    -store: Valid hash value (alpha-numeral)

    """

    zeros='0'*zeros
    store = None
    num = 1000000000
    for i in range(num):
        text = str(block)+transaction+str(hash_prev)+str(i)
        new = generate_sha(text)
        if new.startswith(zeros):
            store = new
            break
    if store is not None:
        print('Mining...')
        time.sleep(0.7)
        print('You have successfully mined a sample bitcoin.')
        time.sleep(0.7)
    return store

def main():
    """
    Parameters:
    -transactions: String of names of customers and arrows indicate direction of transaction (eg: Zoe->Tom->40)
    -level: Number of zeros required before hash
    -prev_hash: Hash key from previous transaction

    """

    start = time.time()
    transaction = input('Enter your transactions: ')
    level = 5
    prev_hash = '0000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7rj1'
    generated = Mine(2,transaction,prev_hash,level)
    end = time.time()
    print('Time taken: {:.2f}'.format(end-start))
    print('Hash value: ',generated)
    print('Thank you for using our interface.')

if __name__=='__main__':
    main()
