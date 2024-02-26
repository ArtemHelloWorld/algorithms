class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter_postfix = dict()
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in counter_postfix:
                counter_postfix[s[i]] = i

        ans = []
        l, r = 0, 0

        for i in range(len(s)):
            r = max(r, counter_postfix.get(s[i], 0))
            if i == r:
                ans.append(r - l + 1)
                l = r + 1
        return ans

