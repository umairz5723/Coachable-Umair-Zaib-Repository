""" 212. Word Search II """

from typing import List

class TrieNode():

    def __init__(self):
        """
        This method initalizes a TrieNode
        storing the letters within, a boolean
        to if it is a valid word, and an interger
        reference for the # of avaliable words 
        in it's path.
        """
        self.children = {}
        self.is_word = False
        self.refs = 0

    def add_word(self, word):
        """
        This method adds a word into the
        Trie data structure, adding to 
        the # of ref's at each node it comes
        across.
        """
        cur = self
        cur.refs += 1
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.refs += 1
        cur.is_word = True

    def remove_word(self, word):
        """
        This method removes a word from
        the Trie data structure, also
        removing the # of ref's at each
        existing node character.
        """
        cur = self
        cur.refs -= 1

        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                cur.refs -= 1



class Solution:
    """ Solution Class """
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        This solution implements a Trie data structure that is used
        to store the input words we are looking for.

        Using this structure, we can search the board for any 
        existings words in our Trie and return them in the 
        results.

        """
        root = TrieNode()

        for word in words:
            root.add_word(word)

        rows = len(board)
        cols = len(board[0])
        visited = set()
        result = set()

        def dfs(r,c,node,word):

            """
            DFS Method to handle searching board
            1) Edgecases handle failed searches
            2) We will use the current letter at board[r][c] to go to the next child node
            to add to the word.
            3) If the node we are on is a word, we can add it to the result, while also
            removing it from the root and marking its isWord flag to false.
            4) Recursively call on all 4 neighbors (top,bottom,right,left) and 
            remove the given (row,column) from visited we complete.
            """

            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited:
                return 
            if board[r][c] not in node.children:
                return
            if node.children[board[r][c]].refs < 1:
                return

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_word:
                result.add(word)
                node.is_word = False
                root.remove_word(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(result)
