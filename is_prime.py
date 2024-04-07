import unittest

def half_number(value):
    if value % 2 != 0:
        half = (value - 1)/2    
        return half
    elif value == 2:
        half = 2/2
        return half
    else:
        return None

def divisible(value):
    divisible = "Divisible"
    all = 0
    value = str(value)
    for i in range(len(value)):
        all += int(value[i])
    if all % 3 == 0 or all % 9 == 0:
        return divisible
    elif len(value) > 2:
        if value[-1] and value[-2] == "0":
            return divisible
    elif int(value[-1]) % 4 == 0:
        return divisible
    elif value[-1] == "0" or value[-1] == "5":
        return divisible
    else:
        return None


def is_prime(value):
    half = half_number(value)
    divided = None
    if value > 3:
        divided = divisible(value)

    if half == None or divided != None:
        return False
    else:
        while half > 1:
            if value % half == 0:
                return False
            else:
                half -= 1
    return True
    
            
    

