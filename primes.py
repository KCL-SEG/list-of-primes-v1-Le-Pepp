"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes >= 1:
        list.append(2)
    if number_of_primes >= 2:
        list.append(3)

    i = 0
    j = 0
    n = 1
    while i < number_of_primes - 2:
        appended = False
        if j % 2 == 0:
            x = 6*n-1
            if x % 5 != 0 or x == 5:
                list.append(x)
                appended = True
        else:
            x = 6*n+1
            if x % 5 != 0:
                list.append(x)
                appended = True
            n += 1
        
        if appended:
            i += 1
        j += 1

    return list

