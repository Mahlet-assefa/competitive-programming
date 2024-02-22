class Solution:
    def minOperations(self, logs: List[str]) -> int:
        arr=[]
        for log in logs:
            if log=="../":
                if arr:
                    arr.pop()
            elif log=="./":
                continue
            else:
                arr.append(log)
                
        return len(arr)