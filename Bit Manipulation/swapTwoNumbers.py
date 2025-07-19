''' For XOR Operator : Even no of 1's -> 0
                        Odd no of 1's -> 1
So the XOR of same number is 0
'''

def swapTwoNumber(x, y):
    x = x^y
    y = x^y
    x = x^y
    print(f"x->{x}, y->{y}")

x = 5
y = 6
swapTwoNumber(x,y)