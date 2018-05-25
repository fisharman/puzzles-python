def min_substring(s, t):
    # two pointers keeping track
    begin, end = 0, 0

    #build map of t
    need_to_find = {}
    for letter in t:
        need_to_find[letter] = need_to_find.get(letter,0) + 1

    has_found = {}
    count = 0
    for letter in s[]: #beginning to end slicing
        if has_found[letter] > need_to_find[letter]:
            has_found[letter] += 1
            count += 1

        if count >= len(t):
            pass
            # found, move beginning pointer


    #print(t_histogram)

min_substring(1,'BANC')