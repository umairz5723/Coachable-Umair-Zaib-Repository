""" 211. Design Add and Search Words Data Structure """

class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:
  
    """
    
    This solution uses the exact same setup from first Trie problem, in that we create TrieNodes of characters
    at each level when needed and mark the final character as a word. The only difference in the search method is the 
    handling of the the "." character in which we must use a dfs function that keeps track of an idx and node. When we match 
    with a "." we check if the next index and child lead to a word and return True/False based on this. Otherwise, we handle
    alphabetical characters the exact same in the first problem.

    """
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.isWord = True


    def search(self, word: str) -> bool:

        def dfs(idx, node):
            cur = node

            for i in range(idx, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if ch not in cur.children:
                        return False
                    cur = cur.children[ch]
            
            return cur.isWord
        
        return dfs(0, self.root)