'''
Problem 1:
given two strings s and t, determine if s is one edit different from t.
one edit: one insert, one delete or one replace
e.g.
s = "refdash", t = "rfdash", return true (one insert of "e" in t)
s = "refdash", t = "refdashs", return true (one delete of "s" in t)
'''


# question:
# input null? treat as normal string
# output type? boolean
# time: 35min

def check_one_diff(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False

    # replace: len(s) == len(t), 1 character different

    # insert: len(t) - len(s) == 1, remaining character are the same

    # delete: len(s) - len(t) == 1, remaining characters are the same

    one_diff = False
    if len(s) == len(t):
        for idx in range(len(s)):
            if s[idx] != t[idx]:
                if one_diff:
                    return False
                one_diff = True
    elif len(t) - len(s) == 1:
        offset = 0
        for idx in range(len(s)):
            if s[idx] != t[idx+offset]:
                if one_diff:
                    return False
                one_diff = True
                offset = 1
                if s[idx] != t[idx + offset]:
                    return False
    else:
        offset = 0
        for idx in range(len(t)):
            if s[idx+offset] != t[idx]:
                if one_diff:
                    return False
                one_diff = True
                offset = 1
                if s[idx+offset] != t[idx]:
                    return False

    return True

if __name__ == "__main__":
    print(check_one_diff("refdash", "refdash"))
    print(check_one_diff("refdash", "refdas"))
    print(check_one_diff("refdas", "refdash"))

    print(check_one_diff("abcd", "abef"))
    print(check_one_diff("abcde", "abcf"))
    print(check_one_diff("abcde", "abcddf"))

    print(check_one_diff("abcdefg", "acdefh"))


'''
s = 'refdash'
t = 'rfdash'
print(check(s, t))

s = "refdash"
t = "refdashs"
print(check(s, t))

s = 'reeras'
t = 'reedas'
print(check(s, t))

s = "refdashs"
t = "refdash"

print(check(s, t))
'''