class Solution:
    """
     1) Добавляем hit только с увеличением времени,
     а если время тоже, увеличиваем счетчик

    2) Для поиска интервала времени используем бинпоиск

    3) Считаем удары префиксной суммой,
    чтобы находить левую и правую границу и вычитать их значения.
    (без префикса пришлось бы суммировать все слева направо)

    """
    def __init__(self):
        self.hits = [[0, 0]]
        self.interval = 300

    def hit(self, timestamp: int) -> None:
        """Prefix summ | Time O(1) | Memory < O(N)"""
        if self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, self.hits[-1][1] + 1])

    def _rBinSearch(self, target: int) -> int:
        l = 0
        r = len(self.hits) - 1
        while l < r:
            m = (r + l + 1) // 2
            if self.hits[m][0] <= target:
                l = m
            elif self.hits[m][0] > target:
                r = m - 1
        return l

    def _lBinSearch(self, target: int) -> int:
        l = 0
        r = len(self.hits) - 1
        while l < r:
            m = (r + l) // 2
            if self.hits[m][0] >= target:
                r = m
            else:
                l = m + 1
        return l

    def getHits(self, right_timestamp: int) -> int:
        """Bin search | Time O(logN) | Memory O(1)"""
        r = self._rBinSearch(right_timestamp)
        left_timestamp = right_timestamp - self.interval
        l = self._lBinSearch(left_timestamp)
        return self.hits[r][1] - self.hits[l][1]  # prefix summ


solution = Solution()
solution.hit(1)
solution.hit(1)
solution.hit(1)
solution.hit(2)
solution.hit(2)
solution.hit(300)
solution.hit(301)
solution.hit(301)
solution.hit(301)
print(solution.hits)
# [[0, 0], [1, 3], [2, 5], [300, 6], [301, 9]]


assert solution.getHits(1) == 3
assert solution.getHits(2) == 5
assert solution.getHits(3) == 5
assert solution.getHits(300) == 6
assert solution.getHits(301) == 6
