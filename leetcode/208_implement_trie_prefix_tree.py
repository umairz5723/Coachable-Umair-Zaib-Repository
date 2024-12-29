"""208. Implement Trie"""
class Node():
    def __init__(self):
        self.map = {}
        self.isWord = False


class Trie:

    def __init__(self):
       self.root = Node()
      
    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if ch not in cur.map:
                cur.map[ch] = Node()
            cur = cur.map[ch]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for ch in word:
            if ch not in cur.map:
                return False
            cur = cur.map[ch]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for ch in prefix:
            if ch not in cur.map:
                return False
            cur = cur.map[ch]
        return True
