class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Если бы были даны отсторитрованные массивы -
        через два указателя идем пока не дойдем до конца одного из массивов
        """
        count1 = dict()
        ans = []

        for x in nums1:
            count1[x] = count1.get(x, 0) + 1

        for x in nums2:
            if count1.get(x, 0) > 0:
                count1[x] -= 1
                ans.append(x)

        return ans