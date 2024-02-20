class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        min_rabbits = 0
        for key, val in count.items():
             min_rabbits += ((key + 1) * ((key + val) // (key + 1)))
        return min_rabbits