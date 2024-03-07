class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=-1
        r=len(letters)-1
        while l+1<r:
            mid=(l+r)//2
            if ord(letters[mid])>ord(target):
                r=mid
            else:
                l=mid
        if ord(letters[r])<=ord(target):
            return letters[0]
        else:
            return letters[r]

