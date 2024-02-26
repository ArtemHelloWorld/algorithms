from collections import defaultdict


class Solution:
    def minWindow(self, string: str, substring: str) -> str:
        substring_dict = defaultdict(int)
        for x in substring:
            substring_dict[x] += 1

        string_dict = defaultdict(int)
        l = 0
        r = 0
        minn, minn_l, minn_r = float('inf'), None, None
        while r < len(string):
            string_dict[string[r]] += 1

            while l < len(string) and string_dict[string[l]] > substring_dict[string[l]]:
                string_dict[string[l]] -= 1
                l += 1
            if minn > r - l + 1:
                for key, value in substring_dict.items():
                    if string_dict[key] < value:
                        break
                else:
                    minn, minn_l, minn_r = r - l + 1, l, r

            r += 1
        return string[minn_l:minn_r + 1] if minn_l is not None else ''



