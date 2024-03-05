class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backgenerateParenthesis(s,l,r):
            if len(s)== n*2:
                ans.append(s)
                return 
            if l<n:
                backgenerateParenthesis(s+"(",l+1,r)
            if r<l:
                backgenerateParenthesis(s+")",l,r+1)
            
       
        backgenerateParenthesis("",0,0)
        return ans
        
                


               