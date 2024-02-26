class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        maxx_i = height.index(max(height))

        ans = 0

        mountains_up = (height[:maxx_i+1], height[maxx_i::][::-1])
        for mountain in mountains_up:
            local_max = 0
            for h in mountain:
                local_max = max(local_max, h)
                ans += local_max - h
        return ans
