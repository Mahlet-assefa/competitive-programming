class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        task=sorted(tasks,key=lambda x:x[1]-x[0],reverse=True)
        total=0
        spent=0
        curr=0
        for i in range(len(task)):
            if curr<task[i][1]:
                total+=task[i][1]-curr
            spent=spent +task[i][0]
            # print(total,spent)
            curr=total-spent
            # print(curr)
            
        return total
