def checkithBitIsSetOrNot(n, i):
    if n & (1<<i) != 0:
        return True
    else:
        return False

n = 13
print(checkithBitIsSetOrNot(n,2))
print(checkithBitIsSetOrNot(n,1))