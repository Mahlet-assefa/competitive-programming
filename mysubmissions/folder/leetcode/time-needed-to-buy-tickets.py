class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque()
        cnt=0
        for i in  range(len(tickets)):
            q.append(i)
        while q:
            temp=q.popleft()
            tickets[temp]-=1
            if tickets[temp] >=1:
                q.append(temp)
            cnt+=1

            if tickets[k] ==0:
                return cnt
        
            
            
        




