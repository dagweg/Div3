class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        me = 0
        piles = sorted(piles)[len(piles)//3:]
        for i in range(len(piles)-2, -1,-2):
            me += piles[i]
        return me
