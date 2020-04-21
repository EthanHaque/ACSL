import math

def main():
    inpt = [int(x) for x in input().split()]
    pieces = inpt[0:6]
    rolls = inpt[7:]

    for r in rolls:
        pieces.sort()
        temp = pieces[0] + r

        if (temp in pieces):
            continue
        elif (isPrime(temp)):
            count = 0
            while (temp < pieces[inbetween(temp, pieces)[1]] - 1 and count < 6):
                temp += 1
        elif (temp in [9, 16, 25, 36, 49]):
            while (temp > pieces[inbetween(temp, pieces)[0]] + 1 and count < 6):
                temp -= 1
        elif (passedCorner(pieces[0], temp)):
            while (temp > pieces[0] and temp % r != 0 or temp in pieces):
                temp -= 1
        
        if (temp == 52):
            pieces[0] = 999
        elif (temp > 52):
            continue
        else:
            pieces[0] = temp
    pieces.sort()
    print(pieces)
        


def inbetween(n, l):
    for count, i in enumerate(l):
        if(i > n):
            return ([count-1, count])
    return ([-1, 1])
        
def isPrime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True

def passedCorner(n1, n2):
    corners = [7, 12, 17, 22, 35, 40, 45, 50]
    if(inbetween(n1, corners) != inbetween(n2, corners)):
        return True
    return False

main()