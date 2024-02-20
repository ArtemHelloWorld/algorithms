class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        count = 0
        ans = [count] * len(A)
        for i in range(len(A)):
            if A[i] in set_b:
                set_b.remove(A[i])
                count += 1
            else:
                set_a.add(A[i])

            if B[i] in set_a:
                set_a.remove(B[i])
                count += 1
            else:
                set_b.add(B[i])
            ans[i] = count
        return ans

