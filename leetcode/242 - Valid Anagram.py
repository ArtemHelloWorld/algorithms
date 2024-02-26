class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        need = set()
        counter = dict()
        for c in s:
            if c not in counter:
                counter[c] = 0
                need.add(c)
            counter[c] += 1

        for c in t:
            if c not in need:
                return False
            counter[c] -= 1
            if counter[c] == 0:
                need.remove(c)

        return len(need) == 0