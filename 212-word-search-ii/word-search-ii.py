from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # store complete word at end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Step 1: Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word   # mark end
        
        # Step 2: DFS function
        def dfs(i, j, node):
            char = board[i][j]
            
            if char not in node.children:
                return
            
            next_node = node.children[char]
            
            # Check if word found
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None  # avoid duplicate
            
            # Mark visited
            board[i][j] = "#"
            
            # Explore 4 directions
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    if board[ni][nj] != "#":
                        dfs(ni, nj, next_node)
            
            # Backtrack
            board[i][j] = char
        
        # Step 3: Start DFS from each cell
        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)
        
        return result