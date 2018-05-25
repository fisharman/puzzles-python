class Node:
    def __init__(self, char: str):
        self.char = char
        self.child = []
        self.word_count = 0
        self.word_end = False


class Autocomplete1:
    def __init__(self):
        self.root = Node("*")

    def find_word(self, current, word, answers):

        if current.word_end:
            answers.append(word)

        for element in current.child:
            self.find_word(element, word+element.char, answers)

    def find(self, partial):
        if partial is None:
            return

        current = self.root
        for let in partial:
            found = False
            for ele in current.child:
                if ele.char == let:
                    found = True
                    current = ele
                    break

            if not found:
                return 0

        answers = []
        self.find_word(current, partial, answers)
        return answers
        # return current.word_count

    def add(self, word):
        if word is None:
            return

        current = self.root
        for let in word:
            found = False
            for child in current.child:
                if child.char == let:
                    found = True
                    current = child
                    break

            if not found:
                current.child.append(Node(let))
                current = current.child[len(current.child)-1]
            current.word_count += 1
        current.word_end = True




class Autocomplete():
    def __init__(self):
        # root contains array
        self.root = {}

    def add(self, word):

        current_node = self.root

        for let in word:
            if let not in current_node:
                current_node[let] = {}
            current_node = current_node[let]
        current_node["end_word"] = True

    def find_words(self, current_node):
        count = 0
        if len(current_node) == 0:
            return 1

        for k in current_node.keys():
            if k == "end_word":
                count += 1
            else:
                count += self.find_words(current_node.get(k))

        return count

    def find(self, partial):
        current_node = self.root

        for let in partial:
            current_node = current_node.get(let)
            if not current_node:
                return 0

        total_count = self.find_words(current_node)

        return total_count


if __name__ == "__main__":
    autocomplete = Autocomplete1()
    autocomplete.add('pies')
    autocomplete.add('pias')
    autocomplete.add('abcdefg')
    autocomplete.add('hack')
    autocomplete.add('hacker')
    print(autocomplete.find('pi'))
    print(autocomplete.find('abcdef'))
    print(autocomplete.find('hac'))