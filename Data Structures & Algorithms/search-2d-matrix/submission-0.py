class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWs, COLs = len(matrix) , len(matrix[0])
        top, bot = 0 , ROWs - 1
        while top <= bot:
            if not (top <= bot):
                return False
            midRow = (top+bot)//2
            if matrix[midRow][-1] < target:
                top = midRow + 1
            elif matrix[midRow][0] > target:
                bot = midRow - 1
            else:
                break
        midRow = (top+bot) // 2
        l,r = 0 , COLs - 1
        while l <= r:
            m = (l+r) // 2
            if matrix[midRow][m] > target:
                r = m - 1 
            elif matrix[midRow][m] < target:
                l = m + 1
            else:
                return True
        return False