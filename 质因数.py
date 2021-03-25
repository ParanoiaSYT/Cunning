



def isZS(x):
    flag = 1
    for i in range(2, int(x**0.5)):
        if x%i == 0:
            flag = 0
            print(str(i),end=' ')
            isZS(int(x/i))
            break
    if flag == 1:
        print(str(x), end = ' ')


isZS(7944871094)