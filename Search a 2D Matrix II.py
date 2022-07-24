class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        row, col = n-1, 0 
        
        while row>=0 and col<m:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                row -= 1
            elif matrix[row][col]<target:
                col += 1
        return False
                
