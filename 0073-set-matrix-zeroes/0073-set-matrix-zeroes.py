class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_index = []
        row_size = len(matrix)
        column_size = len(matrix[-1])

        for row in range(row_size):
            for column in range(column_size):
                if matrix[row][column] == 0:
                    index = (row, column)
                    zero_index.append(index)
        
        for zero in zero_index:
            for row in range(row_size):
                for column in range(column_size):
                    if row == zero[0] or column == zero[1]:
                        matrix[row][column] = 0