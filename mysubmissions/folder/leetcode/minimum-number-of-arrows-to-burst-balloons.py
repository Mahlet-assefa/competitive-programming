class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        point=sorted(points,key=lambda x:x[1])
        #print(point)
        x=0
        end=float('-inf')
        for i in range(len(point)):
            if end < point[i][0]:
                x+=1
                end=point[i][1]
                
        return x

