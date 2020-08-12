import math


def mysqrt(a, x=4):
    while True:
        # print('x >', x)
        y = (x + a/x) / 2
        if y == x:
            print(y)
            break
        x = y



def test_square_root():
    print('a     mysqrt(a)   math.sqrt(a)    diff')
    print('-'*40)
    for i in range(1,10):
        print(f'{i}', end='||'f'{math.sqrt(i)}||')
        mysqrt(i)
        # mysqrt(i)
        # print(end=' ')
        # print(math.sqrt(i))
        


test_square_root()