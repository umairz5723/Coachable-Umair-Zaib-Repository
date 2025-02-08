"""208. Implement Trie (Prefix Tree)"""

# pylint: disable=too-few-public-methods
class TrieNode:
    """Node class for Trie data structure"""
    def __init__(self):
        """Initialize TrieNode with empty character map and word flag"""
        self.char_map = {}  # Changed from map to char_map
        self.is_word = False  # Changed from isWord to is_word

class Trie:
    """Implementation of Trie (Prefix Tree) data structure"""

    def __init__(self):
        """Initialize Trie with root node"""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Args:
            word: String to insert into the trie
            
        Returns:
            None
        """
        cur = self.root
        for char in word:
            if char not in cur.char_map:
                cur.char_map[char] = TrieNode()
            cur = cur.char_map[char]
        cur.is_word = True

    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.
        
        Args:
            word: String to search for
            
        Returns:
            bool: True if word exists in trie, False otherwise
        """
        cur = self.root
        for char in word:
            if char not in cur.char_map:
                return False
            cur = cur.char_map[char]
        return cur.is_word

    def starts_with(self, prefix: str) -> bool:  # Changed from startsWith
        """
        Check if there is any word in the trie that starts with the given prefix.
        
        Args:
            prefix: String prefix to search for
            
        Returns:
            bool: True if any word starts with prefix, False otherwise
        """
        cur = self.root
        for char in prefix:
            if char not in cur.char_map:
                return False
            cur = cur.char_map[char]
        return True
