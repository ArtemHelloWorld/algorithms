class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        y = len(mat)
        x = len(mat[0])
        for k in range(-x, y + 1):
            arr = []
            for i in range(y):
                j = i - k
                if not 0 <= i < y or not 0 <= j < x:
                    continue
                arr.append(mat[i][j])
            arr.sort(reverse=True)
            for i in range(y):
                j = i - k
                if not 0 <= i < y or not 0 <= j < x:
                    continue
                mat[i][j] = arr.pop()
        return mat


"""
i - j = k

     x, j
y, i     
        0  -1  -2  -3
        1   0  -1  -2
        2   1   0  -1 
"""
