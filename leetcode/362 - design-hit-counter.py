class Solution:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])

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
        r = self._rBinSearch(right_timestamp)
        left_timestamp = right_timestamp - 300
        l = self._lBinSearch(left_timestamp)
        return sum(x[1] for x in self.hits[l:r + 1])
