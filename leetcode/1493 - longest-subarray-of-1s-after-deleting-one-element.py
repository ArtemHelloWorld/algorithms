from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = 0
        counter = dict()
        count_0 = 0
        for i, x in enumerate(nums):
            if x == 0:
                count_0 += 1
                counter[count_0] = i
            if count_0 - 1 in counter:
                maxx = max(maxx, i - counter[count_0-1] - 1)
            else:
                maxx = max(maxx, i)
        return maxx
