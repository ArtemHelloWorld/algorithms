class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = 0
        while m != len(nums) - 1:
            if abs(nums[m]) < abs(nums[m + 1]):
                break
            m += 1

        l = m - 1
        r = m
        ans = []
        while l >= 0 and r < len(nums):
            if abs(nums[l]) <= abs(nums[r]):
                ans.append(nums[l] ** 2)
                l -= 1
            else:
                ans.append(nums[r] ** 2)
                r += 1
                
        while l >= 0:
            ans.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            ans.append(nums[r] ** 2)
            r += 1

        return ans

