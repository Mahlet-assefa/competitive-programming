class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        min_rabbits = 0
        for key, val in count.items():
            idrab=((key + val) // (key + 1))
            min_rabbits += (key + 1) * idrab
             
        return min_rabbits