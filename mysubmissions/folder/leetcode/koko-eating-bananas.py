class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=0
        r=max(piles)
        while l+1<r:
            mid=(l+r)//2
            summed=0
            for i in range(len(piles)):
                eated=ceil(piles[i]/mid)
                summed+=eated
            if summed <= h :
                r=mid
                        
            elif summed > h:
                l=mid
        return r
            


                    
                    
                    


