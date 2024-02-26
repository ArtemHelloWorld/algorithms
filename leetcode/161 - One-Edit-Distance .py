class Solution:
    def isOneEditDistance(self, s: str, t: str) -> int:
        if abs(len(s) - len(t)) > 1:
            return False

        l = 0
        while l < min(len(s), len(t)) and s[l] == t[l]:
            l += 1

        r = -1
        while abs(r) <= min(len(s), len(t)) and s[r] == t[r]:
            r -= 1

        if l == len(s) + r or l == len(t) + r:
            return True
        else:
            return False


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m > n:  # Make sure that |s| <= |t|.
            return self.isOneEditDistance(t, s)

        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]  # Replace s[i] with t[i].
                return s[i:] == t[i + 1:]  # Delete t[i].

        return m + 1 == n  # Delete t[-1].
