class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        combo={")":"(","}":"{","]":"["}

        for i in s:
            if i in combo:
                if stk and combo[i]==stk[-1]:
                        stk.pop()
                else:
                    return False
    
            else:
                stk.append(i)
        if not stk:
            return True 
        else:
            return False
        
