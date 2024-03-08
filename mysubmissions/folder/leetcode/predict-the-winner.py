class Solution:
    def predictTheWinner(self, arr: List[int]) -> bool:
        def check(l,r,turn):
            if l > r:
                return 0
            win=0
            if turn:
                left=check(l+1,r,False)+arr[l]
                right=check(l,r-1,False)+arr[r]
                win= max(left,right)
            else:
                left=check(l+1,r, True)-arr[l]
                right=check(l,r-1, True)-arr[r]
                win= min(left,right)
            return win
        return check(0,len(arr)-1,True)>=0
                    



