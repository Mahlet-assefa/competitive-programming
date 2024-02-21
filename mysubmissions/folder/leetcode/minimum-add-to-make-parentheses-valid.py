class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt=0
        openpar=0
        closepar=0

        for i in range(len(s)):
            if s[i]=="(":
                openpar+=1
            if s[i]==")":
                if openpar:
                    openpar-=1
                else:
                    closepar+=1
        return openpar+closepar
            
