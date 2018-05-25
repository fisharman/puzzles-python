import math
import re

def catchup(a, k , p):
    if a >= k:
        return -1

    return math.floor(p/(k-a)+1)


if __name__ == "__main__":
    #n = input()

    print(catchup(3,4,5))
    print(catchup(3,4,0))

    # output = re.search('//.*$', input())
