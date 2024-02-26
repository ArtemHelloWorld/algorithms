"""ДВА РЕШЕНИЯ"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """DP. Time O(n**2) Memory O(n**2)"""
        if len(s) <= 1:
            return s
        dp = [[i == j for j in range(len(s))]  for i in range(len(s))]
        maxx = 1
        l_maxx, r_maxx = 0, 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and ((j - i == 1) or dp[i+1][j-1] == True):
                    dp[i][j] = True
                    if j - i + 1 > maxx:
                        maxx = j - i + 1
                        l_maxx, r_maxx = i, j
        return s[l_maxx:r_maxx+1]
"""
         e       d      a      b      a      d
    e  [True,  False, False, False, False, False]
    d  [False, True,  False, False, False, TRUE ]
    a  [False, False, True,  False, True,  False]
    b  [False, False, False, True,  False, False]
    a  [False, False, False, False, True,  False]
    d  [False, False, False, False, False, True ]
    
    dp[i][j] означает что s[i:j+1] - палиндром
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Time O(n**2) Memory O(n)"""
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str