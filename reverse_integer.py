import math

'''Solution for '''
def reverse(number):
    log = int(math.log(number, 10))
    x = log
    reverse = 0

    while log > -1:
        digit = int(number/10**log)
        number = number - digit*(10**log)
        reverse += digit*(10**(x - log))

        if reverse >= 2**32:
            return 0

        log -= 1

    return reverse