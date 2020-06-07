def from_dec(number, base = 2):
    decoder = []
    if base == 16:
        array = {}
        key = 10

        for value in range(65, 71):
            array[key] = chr(value)
            key += 1
        
        while number >= 1:
                if number % base >= 10:
                    decoder += str(array.get(number % base))
                    number //= base
                else:
                    decoder += str(number % base)
                    number //= base
                    
    while number >= 1:
        decoder.append(str(number % base))
        number //= base
    
    return ''.join(decoder)[::-1]



def to_dec(number, base = 10):
    number = str(number).upper()
    result = 0

    keys = []
    for i in range(0 , len(number)):
        keys.append(i)
    keys = keys[::-1]
    
    values = ''
    for i in enumerate(number):
        values += str(i[1])
    
    decoder = dict(zip(keys , values))
        
    if base == 16:
        array = {}
        key = 10

        for value in range(65, 71): 
            array[key] = chr(value)
            key += 1
        array = {v:k for k, v in array.items()}
       
        for i in decoder:
            if decoder[i].isdigit():
                result += int(decoder[i]) * (base ** int(i))
            else:
                result +=  array[decoder[i]] * (base ** int(i))
    else:
        for i in decoder:
            result += int(decoder[i]) * (base **int(i))
    return result


def dec2bin(number):
    return from_dec(number, 2)
def dec2oct(number):
    return from_dec(number, 8)
def dec2hex(number):
    return from_dec(number, 16)
def bin2dec(number):
    return to_dec(number, 2)
def oct2dec(number):
    return to_dec(number, 8)
def hex2dec(number):
    return to_dec(number, 16)
