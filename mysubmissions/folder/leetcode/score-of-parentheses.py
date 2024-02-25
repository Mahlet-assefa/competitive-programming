class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk=[0]
        val=0
        for i in s:
            if i=="(":
                stk.append(0)
            else:
                x=stk[-1]
                stk.pop()
                if x>0:
                    stk[-1]+=2*x
                else:
                    stk[-1]+=1
                
        return stk[-1]
