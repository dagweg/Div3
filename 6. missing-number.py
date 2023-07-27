# Time: 6 min

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mx = max(nums)
        st = set()
        for n in nums:
            st.add(n)
        for i in range(mx+1):
            if i not in st: return i
        return mx+1
        
