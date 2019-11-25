import sys
import os
import time 



arg = int(sys.argv[1])

def main():
    for i in range(arg):
        os.system("./tmp36raw")
        time.sleep(1)


if __name__ == '__main__' :
    main()

