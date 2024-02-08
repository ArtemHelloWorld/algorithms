from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1 = 0
        i2 = 0
        nums = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                nums.append(nums1[i1])
                i1 += 1
            else:
                nums.append(nums2[i2])
                i2 += 1

        if i1 < len(nums1):
            nums += nums1[i1:]
        else:
            nums += nums2[i2:]
        print(nums)
        if len(nums) % 2 == 1:
            return nums[len(nums) // 2]
        else:
            return (nums[len(nums) // 2 - 1] + nums[(len(nums) // 2)]) / 2


print(Solution().findMedianSortedArrays([], [3, 4]))

