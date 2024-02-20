class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        my_set=set()
        notseq=1
        for i in range(len(rolls)):
            my_set.add(rolls[i])
            if len(my_set)==k:
                notseq+=1
                my_set.clear()
        return notseq

