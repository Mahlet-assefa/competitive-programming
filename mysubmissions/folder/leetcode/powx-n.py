class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n=0-n
            x=1/x
        if n==0:
            return 1
        if n==1:
            return x
        else:
            if n%2==0:
                return self.myPow(x,n//2)**2
            else:
               return self.myPow(x,n//2)**2*x 
            