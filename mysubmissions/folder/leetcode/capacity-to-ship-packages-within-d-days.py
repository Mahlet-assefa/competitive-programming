class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total=sum(weights)
        l=max(weights)
        r=total

        def capacity(mid):
            day_cnt=0
            summed=0
            for i in range(len(weights)):
                summed+=weights[i]
                if summed>mid:
                    summed=weights[i]
                    day_cnt+=1
                elif summed==mid:
                    summed=0
                    day_cnt+=1
            if summed!=0:
                day_cnt+=1
            return day_cnt

        while l<=r:
            mid=(l+r)//2
            if capacity(mid)<=days:
                r=mid-1
            elif capacity(mid)>days:
                l=mid+1
        return l


                   