class Solution:
    def valid_sub_string(self, s: str, l: int, r: int):
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        for i in range((len(s) + 1) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return (self.valid_sub_string(s, i + 1, len(s) - 1 - i) or
                        self.valid_sub_string(s, i, len(s) - 1 - i - 1))
        return True

