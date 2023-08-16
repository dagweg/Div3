class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):
            index_map[num] = i
        
        for first, second in operations:
            index = index_map[first]
            nums[index] = second
            index_map[second] = index
            del index_map[first]
        
        return nums
