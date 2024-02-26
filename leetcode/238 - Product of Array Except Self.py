class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zeroes = 0
        product = 1
        for x in nums:
            if x != 0:
                product *= x
            else:
                count_zeroes += 1

        ans = []
        for x in nums:
            if x == 0:
                if count_zeroes == 1:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                if count_zeroes != 0:
                    ans.append(0)
                else:
                    ans.append(product // x)
        return ans
