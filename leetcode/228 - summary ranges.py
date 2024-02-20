class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums += [float('inf')]
        ans = []
        l = 0
        r = 1
        while r < len(nums):
            if nums[r - 1] + 1 != nums[r]:
                ans.append(str(nums[l]) if r - l == 1 else f'{nums[l]}->{nums[r - 1]}')
                l = r
            r += 1
        return ans