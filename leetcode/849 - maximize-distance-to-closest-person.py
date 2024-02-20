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

