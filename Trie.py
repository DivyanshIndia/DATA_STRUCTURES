"""
A data structure commonly used to represent a dictionary for looking up words in a vocabulary.
Let's see an example:
Consider the task of implementing a search bar with auto-completion or query suggestion.
When a user enters a query, the search bar will automatically suggest common queries starting with the characters input
by the user.

Trie:
Is a tree-like data structure made up of nodes.
Nodes can be used to store data.
Each node may have none, one or more children.
When used to store a vocabulary, each node is used to store a character and consequently each "branch" of the trie
represents a unique word.

                  (root)
                    |
                  ( W )
                    |
                   /\
                  /  \
                 /    \
               (A)   (I)
               /       \
             /          \
            /            \
     (S .end = True)    (S)
                          \
                           \
                           (H, end = True)


How does Trie Work ?
-- There are two major operations that can be performed on a trie
1. Inserting a word into the trie
2. Searching for words using a trie

-- Inserting words into the Trie:
- In order to insert a new word into the trie we need to first check whether any prefix of the word is already in the
trie. Therefore, we will traverse the trie from the root node and follow the algorithm below:
    1. Set the current node to be the root node.
    2. Set the current character as the first character of the input word.
    3. Check if the current character is a child of the current node:
        i. If yes, set the current node to be this child node, set the current character to the next character in the
           input word  and perform this operation again.

        ii. If no, it means from this character onwards , we will need to create new nodes and insert them into the trie


-- Searching in the Trie:
- A common application scenario of the trie data structure is to search for words with the certain prefix, just like the
autocomplete or query suggestion function in a search bar.

- When given a prefix, we can traverse the trie to check if any word in the trie starts with that prefix.
- If the prefix is found in the Trie , we can then use depth-first traversal to retrieve all the words with that prefix.

"""

""" IMPLEMENTING TRIE IN PYTHON """


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end = False

        # a counter indicating how many times a word is inserted (if this node's  self.end = True)
        self.counter = 0
        # a dictionary of child nodes (keys are characters , values are nodes)
        self.children = {}


class Trie:
    def __init__(self):
        # the trie has at least one node --> the root node
        # the root node doesn't store any character
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # if a character is not found, create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # mark the end of the word
        node.end = True
        # Increment the counter to indicate that we see this once more
        node.couter += 1

    def dfs(self, node, prefix):
        """
        Depth-first traversal of the trie.
        :param node:  the node to start with.
        :param prefix: the current prefix for tracing a word while traversing the trie.
        :return: None
        """
        if node.end:
            self.output.append([prefix + node.char, node.counter])

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def query(self, x):
        """ Given an input (a prefix), retrieve all words stored in the trie with that prefix, sort the word by the
        number of times they have been inserted.
        Use the variable within the class to keep all possible outputs as there can be more than one word with such
        prefix.
        """
        self.output = []
        node = self.root

        # check if the prefix is in the trie
        for c in x:
            if c in node.children:
                node = node.children[c]
            else:
                # can't find the prefix , return empty list
                return []

        # Traverse the trie to get all candidates i.e. words starting with the prefix
        self.dfs(node, x[:-1])

        return sorted(self.output, key=lambda x: x[1], reverse=True)

