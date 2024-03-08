class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=-1
        r=len(citations)+1
        while l+1<r:
            mid=(l+r)//2
            temp=bisect_left(citations,mid)
            print(temp)
            if mid<=len(citations)-temp:
                l=mid
            else:
                r=mid
        return l