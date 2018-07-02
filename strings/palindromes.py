def isNumPalindrome(x):
    # x = str(x)
    # return x == x[::-1]

    if (x < 0):
        return False

    tmp = x
    reverse_x = 0
    while(tmp > 0):
        reverse_x = reverse_x*10 + tmp%10
        tmp = tmp // 10
    return x == reverse_x

