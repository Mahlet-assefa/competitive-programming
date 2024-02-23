class Solution:
    def simplifyPath(self, path: str) -> str:
        arr=[]
        res=""
        path+="/"
        for p in range(len(path)):
            if path[p]!="/":
                res+=path[p]
            else:
                if res=="..":
                    if arr:
                        arr.pop()
                elif res!="" and res!=".":

                    arr.append(res)
                res=""
        return "/"+"/".join(arr)


       



          

