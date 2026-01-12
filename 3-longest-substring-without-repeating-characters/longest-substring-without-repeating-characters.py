class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        i = 0
        result = 0

        for j in range(len(s)):
            if s[j] in visited:
                i = max(visited[s[j]], i)

            result = max(result, j - i + 1)
            visited[s[j]] = j + 1

        return result
