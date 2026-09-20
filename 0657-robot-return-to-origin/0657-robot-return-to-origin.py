class Solution(object):
    def judgeCircle(self, moves):
        moved = {
            "U": 0,
            "D": 0,
            "L": 0,
            "R": 0
        }
        for move in moves:
            moved[move] +=  1

        if moved["U"] != moved["D"] or moved["R"] != moved["L"]:
            return False

        return True