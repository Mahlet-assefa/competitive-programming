class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff=sorted(costs,key=lambda x:x[0]-x[1])
        print(diff)
        total=0
        summed=0
        summedb=0
        for i in range(len(diff)):
            if i<len(diff)//2:
                summed+= diff[i][0]
            else:
                summedb+= diff[i][1]
        total=summed+summedb
        return total
        
            
        

