from hashlib import sha256
import time
import random

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

def mineit():
    """
    Parameters:
    -transactions: String of names of customers and arrows indicate direction of transaction (eg: Zoe->Tom->40)
    -level: Number of zeros required before hash
    -prev_hash: Hash key from previous transaction
    """

    start = time.time()
    temp = ['Uchiha->Sasuke->20','Uchicha->Obito->40','Hatake->Kakashi->50','Pasta->Bologanesh->100','Uchicha->Itachi->30','Uzumaki->Naruto->70','Uzumaki->Nagato->40','Hyuga->Hinata->50','Yamanaka->Ino->60','Nara->Shikamaru->75','Guy->Maito->25','Uchicha->Madara->150','Senju->Hashirama->200']
    temp1 = [3,4,5]
    transaction = random.choice(temp)
    level = random.choice(temp1)
    prev_hash = '0000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7rj1'
    generated = Mine(2,transaction,prev_hash,level)
    end = time.time()
    print('(end-start=',(end-start))
    print("generated=",generated)
    '''print('Time taken: {:.2f}'.format(end-start))
    print('Hash value: ',generated)
    print('Thank you for using our interface.')'''
    return (end-start), generated
'''
if __name__=='__main__':
    main()
    '''
