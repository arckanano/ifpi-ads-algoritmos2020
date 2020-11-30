def eval_loop():
    import math
    while True:
        line = input('> ')
        if line == 'done':
            break
        else:
            ava = eval(line)
            print(ava)
    print('Done!')


eval_loop()