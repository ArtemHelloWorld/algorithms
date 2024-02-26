class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        l = 0
        r = 0
        while r < len(chars):
            if chars[l] == chars[r]:
                r += 1
            else:
                chars[count] = chars[l]
                count += 1
                if r - l > 1:
                    for c in str(r - l):
                        chars[count] = c
                        count += 1
                l = r
        chars[count] = chars[l]
        count += 1
        if r - l > 1:
            for c in str(r - l):
                chars[count] = c
                count += 1
        return count

