class Solution:
    def bestClosingTime(self, customers: str) -> int:
        res = 0
        mx = 0
        curr = 0
        for i, x in enumerate(customers):
            if x == 'Y': 
                curr += 1
            else:
                 curr-=1
            if curr > mx:
                mx = curr
                res = i+1
        return res