'''
Below code can be used to convert Positive integers into 
their respective Binaries.


Parameters: a number greater than 0

Output: It will return the Binary value as a string.


Author: K.Hari kiran


'''

def convert_bits(x):
    if x == 0:
        return 0
    base = 2
    quotient = x//base
    power = 0
    bits = {}


    while True:
        if x <= 0:
            break
        elif quotient > 1:
            base *= 2
            power += 1
            quotient = x//base
        elif quotient == 1:
            x = x % base
            power += 1
            bits[power]=1
            power = 0
            base = 2
            quotient = x//base
        else:
            bits[power] = 1
            break


            
    list = []
    for i in range(50):
        list.append (bits.get(i,0))
    list.reverse()
    first = list.index(1)
    newlist = list[first:]


    answer = ''
    for j in newlist:
        answer += str(j)


    return answer

num = int(input("Enter a Positive integer: "))

print("Binary for given number is {0}".format(convert_bits(num)))


