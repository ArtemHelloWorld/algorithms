class Solution:
    def isValid(self, s: str) -> bool:
        opened = '([{'
        closed = ')]}'
        stack = []
        for x in s:
            if x in opened:
                stack.append(x)
            else:
                if not stack or opened.index(stack.pop()) != closed.index(x):
                    return False
        return len(stack) == 0