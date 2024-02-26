class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxx = 0
        l, r = 0, 0
        while r < len(nums):
            k -= nums[r] == 0
            while k < 0:
                k += nums[l] == 0
                l += 1
            maxx = max(r-l+1, maxx)
            r += 1
        return maxx

