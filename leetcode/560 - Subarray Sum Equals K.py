class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        counter = {
            summ: 1
        }
        count = 0
        for x in nums:
            summ += x
            count += counter.get(summ - k, 0)
            counter[summ] = counter.get(summ, 0) + 1

        return count

