class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = 0
        added=0
        total=0
        # print(collections.Counter(s))
        for key, value in collections.Counter(s).items():
            if value % 2 !=0:
                odd += 1
        
        if odd:
            added=1
        total = len(s) - odd + added
        return total