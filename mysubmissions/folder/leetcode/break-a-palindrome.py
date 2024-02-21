class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # checker="abcdefghijklmnopqrstuvwxyz"
        # checker=list(string.ascii_lowercase)
        
        checker2=[]
        checker=[]
        output=""
        n=len(palindrome)

        k=len(palindrome)//2
        for i in range(k):
            checker2.append(palindrome[i])
        #print(checker2)
        if n==1:
            output=""

        else:
            for i in palindrome:
                checker.append(i)
            #print(checker)
            for i in range(len(checker)//2):
                if checker[i]!="a":
                   checker[i] ="a"
                   break
                if checker2.count('a')==n//2 :
                        checker[-1] ="b"    
            for i in range(len(checker)):
                output+=checker[i]
        return output
        
