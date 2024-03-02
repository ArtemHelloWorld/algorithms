class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """Два указателя | Время О(N) | Память O(1)"""
        maxx = 0
        l = 0
        r = 0
        while r < len(seats):
            if seats[r] == 1:
                if l == 0:
                    maxx = max(maxx, r)  # case [0 0 0 0 1 ...]
                else:
                    maxx = max(maxx, (r - l + 1) // 2)
                l = r + 1
            r += 1

        if l != len(seats):
            maxx = max(maxx, r - l)  # case  [... 1 0 0 0 0]
        else:
            maxx = max(maxx, (r - l + 1) // 2)
        return maxx


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """Префиксная сумма | Время О(N) | Память O(N)"""
        right = [0] * len(seats) + [float('inf')]
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 0:
                right[i] = right[i + 1] + 1

        left = [float('inf')] + [0] * len(seats)
        for i in range(len(seats)):
            if seats[i] == 0:
                left[i + 1] = left[i] + 1

        ans = 0
        for i in range(len(seats)):
            closest_distance = min(right[i], left[i + 1])
            ans = max(ans, closest_distance)
        return ans

