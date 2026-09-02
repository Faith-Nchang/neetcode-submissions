class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxS = 0
        visited = set()
        l = 0

        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1

            visited.add(s[r])

            maxS = max(maxS, r - l + 1)
        return maxS


           