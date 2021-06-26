'''
Below code is used to visualize all possible valid Combinations of 
given number of pairs of brackets.


Parameters: a number(i.e num of pairs of brackets)

Output: It will print all possible valid combinations of given number of pairs


Author: K.Hari kiran

Example: 
Input: number of pairs = 3

Output: 
        ((()))
        (()())
        (())()
        ()(())
        ()()()

'''



number_of_pairs = int(input("Enter the number of pairs: "))
if number_of_pairs <= 0:
    print("Please Enter a number greater than 0(Zero).")

def is_valid(strg):
    b_list=[]
    for z in strg:
        if z == '(':
            b_list.append('(')
        else:
            if len(b_list) == 0:
                return False
            else:
                b_list.pop()
    if len(b_list) != 0:
        return False
    return True


counter = 0
repeat = 0
valid = 0
check = 0
list_1 = ['(',')']
list_2 = ['(',')']


for i in range(1,number_of_pairs*2):
    repeat += 2**i
for a in range(1, (number_of_pairs*2)-1):
    check += 2**a


for j in range(repeat):
    for k in list_2:
        bracket = list_1[0]+k
        if counter < check:
            list_1.append(bracket)
        elif is_valid(bracket)==True:
            list_1.append(bracket)
    list_1.remove(list_1[0])
    counter += 1


for b in list_1:
    if is_valid(b) == True:
        valid += 1
        print(b)
    else:
        pass
print("Total Valid Bracket Combinations are {}".format(valid))
