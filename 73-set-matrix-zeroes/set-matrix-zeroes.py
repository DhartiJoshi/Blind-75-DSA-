class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        firstRowZero = False
        firstColZero = False

        
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

       
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 4: set cells to zero using markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 5: update first row
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 6: update first column
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
