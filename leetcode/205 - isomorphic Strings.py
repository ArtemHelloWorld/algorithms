class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}
        set_t = set()
        for i in range(len(s)):
            if s[i] not in dictionary:
                if t[i] in set_t:
                    return False
                dictionary[s[i]] = t[i]
                set_t.add(t[i])
            else:
                if dictionary[s[i]] != t[i]:
                    return False
        return True