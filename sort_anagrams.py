# OUTPUT
# [
#   ['xxy'],
#   ['cab', 'bca’, 'bac'],
#   ['dash', 'shad']
# ]

def sort_letters(word):
    return ''.join(sorted(word))


def sort_anagrams(anagrams):
    output_dict = {}
    for word in anagrams:
        key = sort_letters(word)
        if key in output_dict:
            output_dict[key].add(word)  # duplicates are auto removed in a set
        else:
            output_dict[key] = {word}

    return output_dict
    '''
    output_dict = {}
    i = 0
    for element in sorted_anagrams:
        if element not in output_dict:
            output_dict[element] = []
            output_dict[element].append(anagrams[i])
        elif anagrams[i] not in output_dict[element]:
            output_dict[element].append(anagrams[i])
        i += 1
    '''


anagrams = ['xxy', 'cab', 'bca', 'cab', 'bac', 'dash', 'shad']

for key, value in sort_anagrams(anagrams).items():
    print(value)