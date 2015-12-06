import hashlib

input = 'ckczppom'

def puzzle7():
    counter = 1
    while True:
        hash = hashlib.md5((input + str(counter)).encode('utf-8')).hexdigest()
        if hash[:5] == '00000':
            return counter
        counter = counter + 1

def puzzle8():
    counter = 1
    while True:
        hash = hashlib.md5((input + str(counter)).encode('utf-8')).hexdigest()
        if hash[:6] == '000000':
            return counter
        counter = counter + 1
