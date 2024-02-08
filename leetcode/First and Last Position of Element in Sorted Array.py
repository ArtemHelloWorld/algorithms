from typing import List


class Solution:
    def lbinsearch(self, nums, target, r):
        l = 0
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l

    def rbinsearch(self, nums, target, l):
        r = len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m
        return l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            return [-1, -1] if nums[0] != target else [0, 0]

        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return [
                    self.lbinsearch(nums, target, m),
                    self.rbinsearch(nums, target, m)
                    ]
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m
        return [-1, -1]

print(Solution().searchRange([5,7,7,8,8,10], 8))