"""
Дано бинарное дерево, в вершинах записаны маленькие латинсткие буквы. вершины называются
эквивалентными, если в их поддеревьях одинаковое множество букв (без учета повторений). вернуть
две эквивалентых вершины с максимальным суммарным размером поддеревьев (вершины разные).
"""
class TreeNode:
    def __init__(self, val='', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root) -> set:
        if not root:
            return set()
        ans = set(root.val) | self.dfs(root.left) | self.dfs(root.right)
        self.sets.append(ans)
        return ans

    def func(self, root) -> bool:
        self.sets = []
        self.dfs(root)
        return self.sets

C1 = TreeNode('C')
D1 = TreeNode('D')
B1 = TreeNode('B', C1, D1)

D2 = TreeNode('D')
B2 = TreeNode('B')
C2 = TreeNode('C', D2)
A2 = TreeNode('A', B2, C2)

A3 = TreeNode('A', B1, A2)

print(Solution().func(A3))
