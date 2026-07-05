class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        is_bulky, is_heavy = False, False
        if (length >= 10**4) or (width >= 10**4) or (height >= 10**4) or (length * width * height >= 10**9): is_bulky = True
        if mass >= 100: is_heavy = True

        if is_bulky and is_heavy: return "Both"
        elif is_bulky: return "Bulky"
        elif is_heavy: return "Heavy"
        else: return "Neither"