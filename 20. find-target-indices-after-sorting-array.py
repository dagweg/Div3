class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # O(n) solution
        counts = [0] * 101
        for elem in nums:
            counts[elem] += 1
        for i in range(1,101):
            counts[i] += counts[i-1]
        ret = []
        for i in range(counts[target-1],counts[target]):
            ret.append(i)
        return ret
