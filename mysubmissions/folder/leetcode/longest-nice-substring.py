class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def look(s):
            for i in s:
                if i.lower() in s and i.upper() in s:
                    pass
                else:
                    return False
            return True        
        res=""
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if look(s[i:j+1]) and len(res)<len(s[i:j+1]):
                    res=s[i:j+1]
        return res