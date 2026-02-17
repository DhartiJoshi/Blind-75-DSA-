class Trie:

    def __init__(self):
        # Each node contains:
        # children -> dictionary to store next characters
        # isEnd -> to check if word ends here
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        
        for char in word:
            # If character not present, create new Trie node
            if char not in node.children:
                node.children[char] = Trie()
            
            # Move to next node
            node = node.children[char]
        
        # Mark end of word
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Word must end exactly here
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # If prefix exists, return True
        return True
