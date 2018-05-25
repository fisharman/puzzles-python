"""
1. take the first digit of the string, then recursively call the function with remaining string
2. when the function returns, take the 1st digit from step 1, add the subsequent digit (so the number is now 2 digits),
    then recursively call the function with remaining string
3. stop the recursion when:
    a. there are 7 numbers in the ticket and input string is empty. append ticket to list
    b. there are 7 numbers in the ticket and input string still have numbers left. backtrack.
    c. there are < 7 numbers in the ticker and input string is empty. backtrack.

Time complexity: 2^7
each recursion will create two nodes. the recursion call itself 7 times.
therefore each level will have (2 * previous level nodes) of nodes
"""

# assumption: 1. invalid numbers return empty list 2. if there are more than one answers, return all of them

def ticket_numbers(num):
    if len(num) < 7:
        return []

    seen = set()
    answer = []
    position = 0
    ticket_num = ""

    _ticket_numbers_recursive(num, seen, ticket_num, answer, position)

    return answer


def _ticket_numbers_recursive(num, seen, ticket_num, answer, position):
    valid_range = range(1, 60)
    # if there are numbers left over after 7 digits
    if position >= 7 and len(num) > 0:
        return

    # make sure there are enough numbers left
    if position < 7 and len(num) <= 0:
        return

    # valid ticket number
    if position == 7 and len(num) == 0:
        answer.append(ticket_num.strip())
        return

    for idx in range(1,3):
        if num[0:idx] not in seen and int(num[0:idx]) in valid_range and idx <= len(num):
            # ^make sure it doesn't already exist
            # pass on the remaining numbers to the function
            # if this branch doesn't work out, need to remove number tried from the set
                seen.add(num[0:idx])
                _ticket_numbers_recursive(num[idx:], seen, ticket_num + num[0:idx] + " ", answer, position + 1)
                seen.remove(num[0:idx])
    return


if __name__ == "__main__":
    lottery_list = ["569815571556", "4938532894754", "1234567", "472844278465445", "12", "0", "34125678"]
    # [49 38 53 28 9 47 54]
    for case in lottery_list:
        print(ticket_numbers(case))