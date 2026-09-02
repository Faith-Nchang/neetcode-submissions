class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        res, resLen = 0, 0
        
        for i in range(len(s)):
            # Odd length palindrome
            step, oddLength = 0, 0
            while i - step >= 0 and i + step < len(s) and s[i - step] == s[i + step]:
                oddLength = 2 * step + 1
                if oddLength > resLen:
                    res = i - step
                    resLen = oddLength
                step += 1
            
            # Even length palindrome
            step, evenLength = 0, 0
            while i - step >= 0 and i + step + 1 < len(s) and s[i - step] == s[i + step + 1]:
                evenLength = 2 * (step + 1)
                if evenLength > resLen:
                    res = i - step
                    resLen = evenLength
                step += 1
        
        return s[res: res + resLen]
