class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        counter = dict()
        need = set()
        for s in s1:
            if s not in counter:
                counter[s] = 1
                need.add(s)
            else:
                counter[s] += 1

        l = 0
        r = 0
        while r < len(s1):
            val = s2[r]
            if val in counter:
                counter[val] -= 1
                if counter[val] == 0:
                    need.remove(val)
                elif val not in need:
                    need.add(val)
            r += 1

        if len(need) == 0:
            return True

        while r < len(s2):
            valr = s2[r]
            vall = s2[l]

            if valr in counter:
                counter[valr] -= 1
                if counter[valr] == 0:
                    need.remove(valr)
                elif valr not in need:
                    need.add(valr)

            if vall in counter:
                counter[vall] += 1
                if counter[vall] == 0:
                    need.remove(vall)
                elif vall not in need:
                    need.add(vall)

            if len(need) == 0:
                return True

            l += 1
            r += 1
        return False
