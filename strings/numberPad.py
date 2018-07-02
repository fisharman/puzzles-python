mappings = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def letterCombo(digits):
    if len(digits) < 1:
        return []
    
    if digits[0] not in mappings:
        return []

    q = mappings[digits[0]].copy()    

    for i in digits[1:]:
        if i not in mappings:
            return []
        for _ in range(len(q)):
            current = q.pop(0)
            for letter in mappings[i]:
                q.append(current + letter)

    return q

def letterCombo_recursive(digits):
    list = []
    letterCombo_recursive_h(digits, '', list)
    return list

def letterCombo_recursive_h(digits, current, list):
    if digits == '':
        list.append(current)
        return

    for letter in mappings[digits[0]]:
        letterCombo_recursive_h(digits[1:], current + letter, list)

print(letterCombo_recursive('23'))
print(letterCombo_recursive('5'))
print(letterCombo_recursive('2'))

print(letterCombo('23'))
print(letterCombo('2'))
print(letterCombo('5'))
print(letterCombo('2'))