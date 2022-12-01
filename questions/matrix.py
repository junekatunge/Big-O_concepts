class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get the number of rows and columns 
        ROWS = len(matrix)
        COLS = len(matrix[0])#the matrix is always going to be non-empty that is it cant be zero
        
        top = 0
        # the number of rows minus 1
        bot = ROWS -1
        
        while top <= bot:
            row = (top + bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
#                 no target value is found on the matrix on the bottom and top row
        if not (top<=bot):
            return False
        row = (top + bot)//2
        l = 0
        # the position of r is the number of columns minus 1
        r = COLS - 1
        while l <= r:
            m = (l + r)//2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False