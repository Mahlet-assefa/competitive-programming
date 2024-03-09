class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        idx=collections.deque(range(n))
        ans=[None]*n

        deck.sort()
        for i in deck:
            ans[idx.popleft()]=i
            if idx:
                idx.append(idx.popleft())
        return ans