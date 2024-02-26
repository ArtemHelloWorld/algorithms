class Solution:
    def findAnagrams(self, s1: str, s2: str) -> List[int]:
        if len(s1) < len(s2):
            return []

        counter = dict()
        need = set()
        for s in s2:
            if s not in counter:
                counter[s] = 1
                need.add(s)
            else:
                counter[s] += 1
        ans = []
        l = 0
        r = 0
        while r < len(s2):
            val = s1[r]
            if val in counter:
                counter[val] -= 1
                if counter[val] == 0:
                    need.remove(val)
                elif val not in need:
                    need.add(val)
            r += 1

        if len(need) == 0:
            ans.append(l)

        while r < len(s1):
            valr = s1[r]
            vall = s1[l]

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
            l += 1
            r += 1

            if len(need) == 0:
                ans.append(l)

        return ans