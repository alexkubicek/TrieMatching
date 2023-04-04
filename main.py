import sys


class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char, count):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many nodes have been inserted
        self.counter = count

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

    def print(self, prev):
        print(str(prev) + " " + str(self.counter) + " " + self.char)
        for n in self.children.values():
            n.print(self.counter)


def trie_construction(patterns_c):
    count = 0
    root = TrieNode("", count)
    count += 1
    for pattern in patterns_c:
        current_node = root
        for c in pattern:
            if c not in current_node.children.keys():
                current_node.children[c] = TrieNode(c, count)
                count += 1
            current_node = current_node.children.get(c)
        current_node.is_end = True
    return root


def prefix_trie_matching(text, tri):
    matches = []
    cur = tri
    pattern = str()
    no_match = False
    for c in text:
        if c in cur.children.keys():
            cur = cur.children[c]
            pattern += c
        else:
            no_match = True
            break
        if not no_match and cur.is_end:
            matches.append(pattern)
    return matches


def trie_matching(text, trie_m):
    i_m = 0
    my_dict = {}
    while len(text) > 0:
        matches_found = prefix_trie_matching(text, trie_m)
        for match in matches_found:
            if match not in my_dict.keys():
                my_dict[match] = []
            my_dict[match].append(i_m)
        text = text[1:]
        i_m += 1
    return my_dict


if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    patterns = []
    for line in inFile:
        patterns.extend(line.split())
    inFile.close()
    genome = patterns[0]
    patterns.pop(0)
    trie = trie_construction(patterns)
    dictionary_matches = trie_matching(genome, trie)
    for p in patterns:
        if p not in dictionary_matches.keys():
            dictionary_matches[p] = []
    f = open("output.txt", 'w')
    sys.stdout = f
    starting_positions = set()
    for key in dictionary_matches.keys():
        print(key, end=": ")
        dictionary_matches[key] = [*set(dictionary_matches[key])]
        for i in dictionary_matches[key]:
            # starting_positions.add(i)
            print(i, end=" ")
        print()
    starting_positions = sorted(starting_positions)
    # for pos in starting_positions:
        # print(pos, end=" ")
    f.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
