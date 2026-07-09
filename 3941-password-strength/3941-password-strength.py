class Solution(object):
    def passwordStrength(self, password):
        password = set(password)
        points = 0
        
        for char in password:
            if "a" <= char <= "z": points += 1
            elif "A" <= char <= "Z": points += 2
            elif "0" <= char <= "9": points += 3
            else: points += 5

        return points