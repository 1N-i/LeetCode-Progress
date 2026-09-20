class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        dist = 0
        map_moves = {}
        for move in moves:
            if move == "_": continue
            map_moves[move] = map_moves.get(move, 0) + 1

        if map_moves == {}: return len(moves)

        most_moved = max(map_moves, key=map_moves.get)
        for move in moves:
            if move == "_": move = most_moved
            if move == "L": dist -= 1
            elif move == "R": dist += 1

        if dist < 0: dist *= -1
        return dist