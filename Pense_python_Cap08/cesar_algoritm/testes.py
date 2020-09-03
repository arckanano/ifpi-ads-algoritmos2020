from time import sleep
def main():

    i = 97
    while True:
        print(chr(i))
        sleep(0.3)
        if i == 122:
            i = 96
        i += 1


main()