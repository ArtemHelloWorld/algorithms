import re
class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r'^\s*(?<number>[+|-]?[0-9]+).*$'
        # \s any whitespace
        # . any symbol
        # ? one or zero
        # * many or zero
        # + many or one
        # https://regex101.com/

        res = re.search(pattern, s)
        if res:
            res = int(res.group('number'))
            if res < (-2) ** 31:
                return (-2) ** 31
            elif res > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return res
        else:
            return 0



class Solution:
    def converter(self, s) -> int:
        if not any(x.isnumeric() for x in s):
            return 0

        s = int(''.join(s))
        if s < (-2) ** 31:
            return (-2) ** 31
        elif s > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return s

    def myAtoi(self, s: str) -> int:
        ans = []
        for i, x in enumerate(s):
            if ans:
                if x.isnumeric():
                    ans.append(x)
                else:
                    return self.converter(ans)
            else:
                if x.isspace():
                    continue
                if x.isnumeric() or x == '+' or x == '-':
                    ans.append(x)
                else:
                    return 0
        return self.converter(ans) if ans else 0



