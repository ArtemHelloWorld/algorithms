class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        counter = dict()
        ans = float('-inf')

        while r < len(s):
            if s[r] in counter and counter[s[r]] + 1 > l:
                l = counter[s[r]] + 1
            counter[s[r]] = r
            ans = max(ans, r - l + 1)
            r += 1
        return ans
