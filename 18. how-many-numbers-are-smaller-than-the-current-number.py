class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101

        for n in nums:
            count[n] += 1

        for i in range(1,101):
            count[i] += count[i-1]

        ret = []
        for num in nums:
            if num == 0:
                ret.append(0)
            else:
                ret.append(count[num-1])
        return ret
