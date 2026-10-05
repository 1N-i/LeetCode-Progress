class Solution(object):
    def gameOfLife(self, board):
        ans = []
        len_board = len(board)
        for y in range(len_board):
            row_to_add = []
            row = board[y]
            len_row = len(row)
            for x in range(len_row):
                live_n = 0
                if x-1 >= 0 and row[x-1] == 1:
                    live_n += 1
                if x+1 < len_row and row[x+1] == 1:
                    live_n += 1
                if y-1 >= 0 and board[y-1][x] == 1:
                    live_n += 1
                if y+1 < len_board and board[y+1][x] == 1:
                    live_n += 1
                if (y-1 >= 0 and x-1 >= 0) and board[y-1][x-1] == 1:
                    live_n += 1
                if (y-1 >= 0 and x+1 < len_row) and board[y-1][x+1] == 1:
                    live_n += 1
                if (y+1 < len_board and x-1 >= 0) and board[y+1][x-1] == 1:
                    live_n += 1
                if (y+1 < len_board and x+1 < len_row) and board[y+1][x+1] == 1:
                    live_n += 1

                if row[x] == 0:
                    if live_n == 3:
                        row_to_add.append(1)
                        continue
                    else:
                        row_to_add.append(0)
                        continue
                else:
                    if live_n < 2:
                        row_to_add.append(0)
                        continue
                    elif live_n == 2 or live_n == 3:
                        row_to_add.append(1)
                        continue
                    elif live_n > 3:
                        row_to_add.append(0)
                        continue

            ans.append(row_to_add)
        board[:] = ans