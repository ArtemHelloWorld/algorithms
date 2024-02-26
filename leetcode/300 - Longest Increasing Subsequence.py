class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Time O(NLogN)"""
        ans = [nums[0]]
        for x in nums:
            if x > ans[-1]:
                ans.append(x)
            else:
                i = self.lbinsearch(ans, x)
                ans[i] = x
        return len(ans)
    
    def lbinsearch(self, arr, target):
        l = 0
        r = len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] >= target:
                r = m
            else:
                l = m + 1
        return l


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Time O(N^2)"""
        dp = [0] * len(nums)

        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1
