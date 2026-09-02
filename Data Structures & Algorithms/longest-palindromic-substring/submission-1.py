class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        res, resLen = 0, 0
        
        for i in range(len(s)):
           # odd
            l, r = i, i
            while l>=0 and r < len(s) and s[l] == s[r]:
              if (r - l + 1) > resLen:
                res = l
                resLen = r - l + 1
              l-= 1
              r+=1
            # eveb
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = l
                    resLen = r - l + 1
                l-=1
                r+=1
        return s[res: res+resLen]