class Solution(object):
    def finalValueAfterOperations(self, operations):
        X = 0
        for command in operations:
            if command == "X++" or command == "++X": X += 1
            else: X -= 1
        
        return X