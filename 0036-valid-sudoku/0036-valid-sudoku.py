class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. 행에서 중복된 값이 없는지 찾는다
        # 2. 열에서 중복된 값이 없는지 찾는다
        # 3. 3x3 안에서 중복된 값이 없는지 찾는다 -> i % 3 == 0 일 때만 실행

        column_board_checker = []
        row_board_checker = []

        for column in range(len(board)):
            column_board_checker.clear()
            row_board_checker.clear()
            for row in range(len(board)):
                # 3x3 안에서 중복된 값 확인
                if row % 3 == 0 and column % 3 == 0:
                    area_board_checker = []
                    for area_column in range(column, column + 3):
                        for area_row in range(row, row + 3):
                            print(area_column, area_row)
                            target = board[area_column][area_row]
                            if target != "." and target in area_board_checker:
                                return False
                            else:
                                area_board_checker.append(target)

                column_target = board[row][column]
                row_target = board[column][row]
                if column_target != ".":
                    if column_target in column_board_checker:
                        return False
                    else:
                        column_board_checker.append(column_target)
                    
                if row_target != ".":
                    if row_target in row_board_checker:
                        return False
                    else:
                        row_board_checker.append(row_target)

        return True          