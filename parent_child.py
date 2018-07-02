"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple
generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique
integer identifier.

For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
1   2   4
 \ /   / \
  3   5   8
   \ / \   \
    6   7   9
given a list of pairs, print out all of the children with only 1 known parent and 0 known parents

input = [
    [1, 3], [2, 3], [3, 6], [5, 6],
    [5, 7], [4, 5], [4, 8], [8, 9], [6,10]
];

output = [
  [5, 8, 7, 9],
  [1, 2, 4]
]

2nd part of the question is to find if given 2 children, they have a common ancestor
3, 4 => false
5, 8 => true

3rd part is given a child, their earliest known ancestor -- the one at the farthest distance from the input individual.
If there is more than one ancestor tied for “earliest”, return any one of them. If the input individual has no parents,
the function should return null (or -1).
"""

# cyclic condition?


class Generations:
    def __init__(self):
        self.relationship = {}
        self.ancestor = {}

    def add(self, pair: list) -> None:
        self.relationship.setdefault(pair[0], 0)
        child_count = self.relationship.setdefault(pair[1], 0)
        self.relationship[pair[1]] = child_count + 1

        ancestor_chain = self.ancestor.setdefault(pair[1],[])
        ancestor_chain.append(pair[0])

    # sort and arrange by value??
    def parents_count(self, val: int) -> list:
        output = []
        for individual, parents in self.relationship.items():
            if parents == val:
                output.append(individual)
        return output

    def ancestors(self, child1: int, child2: int) -> bool:
        ancestors1, ancestors2 = [], []
        self._ancestor_search(child1, ancestors1)
        self._ancestor_search(child2, ancestors2)
        return bool(set(ancestors1) & set(ancestors2))

    def _ancestor_search(self, child: int, ancestors: list) -> None:
        if child in self.ancestor:
            ancestor_list = self.ancestor[child]
            for num in ancestor_list:
                ancestors.append(num)
                self._ancestor_search(num, ancestors)


if __name__ == "__main__":
    gen = Generations()
    graph = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 9], [6, 10]]
    for pair in graph:
        gen.add(pair)

    print(gen.parents_count(1))
    print(gen.parents_count(0))
    print(gen.ancestors(6, 8))
    print(gen.ancestors(3, 4))
