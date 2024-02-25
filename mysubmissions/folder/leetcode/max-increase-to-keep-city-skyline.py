class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        summed=0
        rowmaxi=[]
        colmaxi=[]
        for i in range(len(grid)):
            maxii=float("-inf")
            for j in range(len(grid[i])):
                r=grid[i][j]
                maxii=max(maxii,r)
            rowmaxi.append(maxii)

        for j in range(len(grid[i])):
            maxii=float("-inf")
            for i in range(len(grid)):
                r=grid[i][j]
                maxii=max(maxii,r)
            colmaxi.append(maxii)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                k=min(rowmaxi[i],colmaxi[j])
                summed+=k-grid[i][j]
        return summed

        

        
                
                