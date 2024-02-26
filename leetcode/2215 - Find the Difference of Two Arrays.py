class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l = 0
        r = 0
        ans1 = []
        ans2 = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                value = nums1[l]
                while l < len(nums1) and nums1[l] == value:
                    l += 1
                while r < len(nums2) and nums2[r] == value:
                    r += 1
            elif nums1[l] < nums2[r]:
                value = nums1[l]
                ans1.append(value)
                while l < len(nums1) and nums1[l] == value:
                    l += 1
            else:
                value = nums2[r]
                ans2.append(value)
                while r < len(nums2) and nums2[r] == value:
                    r += 1
        while l < len(nums1):
            value = nums1[l]
            ans1.append(value)
            while l < len(nums1) and nums1[l] == value:
                l += 1
        while r < len(nums2):
            value = nums2[r]
            ans2.append(value)
            while r < len(nums2) and nums2[r] == value:
                r += 1
        return ans1, ans2
