class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of seen characters
        seen = set()

        # default return
        longest_subs = 0

        l = 0
        # increase window size
        for r in range(len(s)):
            # shrink window
            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            window_size = r - l + 1

            longest_subs = max(window_size, longest_subs)

        return longest_subs

        