def iterative_sum(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

def recursive_sum(a, b):
    if a == b:
        return b

    return a + recursive_sum(a+1, b)

def tail_recursive_sum(sum, a, b):
    if a == b:
        sum += b
        return sum

    sum += a
    return tail_recursive_sum(sum, a+1, b)


if __name__ == "__main__":
    a = 1
    b = 8
    print(iterative_sum(a,b))
    print(recursive_sum(a,b))
    print(tail_recursive_sum(a, a+1, b))
    #1 + 2 + 3 + 4 = 10
    