class Solution:
    
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        if rowIndex==0:
           return [1]
             
        if rowIndex==1:
            return  [1]*(rowIndex+1)
        arr=[1]
        before=self.getRow(rowIndex-1)
        for i in range(len(before)-1):
            res=before[i]+before[i+1]
            arr.append(res)
        arr.append(1)
        return arr


    
    
    