class Solution(object):
    def spiralOrder(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        x, y = 0, 0

        l_up, l_down = 0, rows - 1
        l_left, l_right = 0, cols - 1
        direction = "right"

        ans = []
        total = rows * cols
        while len(ans) < total:
            ans.append(matrix[y][x])
            if direction == "right":
                if x == l_right:
                    l_up += 1
                    y += 1
                    direction = "down"
                else:
                    x += 1

            elif direction == "down":
                if y == l_down:
                    l_right -= 1
                    x -= 1
                    direction = "left"
                else:
                    y += 1

            elif direction == "left":
                if x == l_left:
                    l_down -= 1
                    y -= 1
                    direction = "up"
                else:
                    x -= 1

            elif direction == "up":
                if y == l_up:
                    l_left += 1
                    x += 1
                    direction = "right"
                else:
                    y -= 1

        return ans