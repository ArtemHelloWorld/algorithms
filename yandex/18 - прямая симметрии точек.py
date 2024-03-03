class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        minn_x, maxx_x = float('inf'), float('-inf')
        points_set = set()
        for x, y in points:
            minn_x = min(minn_x, x)
            maxx_x = max(maxx_x, x)
            points_set.add((x, y))

        summ_x = minn_x + maxx_x
        for x, y in points:
            if not (summ_x - x, y) in points_set:
                return False
        return True
    