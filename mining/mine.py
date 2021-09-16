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
