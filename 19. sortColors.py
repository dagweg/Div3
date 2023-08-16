class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            minIndex = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
