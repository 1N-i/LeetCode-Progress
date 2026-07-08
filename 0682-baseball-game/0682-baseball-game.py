class Solution(object):
    def calPoints(self, operations):
        result = []

        for command in operations:
            if command == "+": result.append(result[-1] + result[-2])
            elif command == "D": result.append(result[-1] * 2)
            elif command == "C": result.pop()
            else: result.append(int(command))

        return sum(result)