class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for x in intervals:
            if not ans:
                ans.append(x)
            else:
                if ans[-1][1] >= x[0]:
                    ans[-1][1] = max(ans[-1][1], x[1])
                else:
                    ans.append(x)
        return ans
