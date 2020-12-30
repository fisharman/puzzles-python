# https://leetcode.com/problems/word-break-ii/discuss/
def word_break(s, wordDict, sentence):
    # insert space and check if word in dict
    # if not, expand word
    # if it is, put the word in list, and call function again
    i = 1
    while i <= len(s):
        if s[:i] in wordDict:
            sentence.append(s[:i])
            word_break(s[i:], wordDict, sentence)
        i += 1


s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
sentence = []

word_break(s, dict, sentence)
print(sentence)


# https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
def bit_difference(a, b):
    diff_sum = 0
    diff = a ^ b
    while diff > 0:
        if diff & 1 == 1:
            diff_sum += 1
        diff = diff >> 1

    return diff_sum


def check_all(arr):
    sum_diff = 0
    for i in arr:
        for j in arr:
            sum_diff += bit_difference(i, j)
    return sum_diff


arr = [1, 2]
arr = [1, 3, 5]

print(check_all(arr))


# https://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0

# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

# https://practice.geeksforgeeks.org/problems/maximum-index/0

# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/