class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict= {"2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz" }
        if len(digits)==0 :
            return 

        def backletterCombinations(digits,added):
            if not digits:
                ans.append(added)
            else:
                for i in my_dict[digits[0]]:
                    backletterCombinations(digits[1:], added + i)
        ans=[]
        backletterCombinations(digits,"")
        return ans
        
                
                
          
        
          
            
            
        