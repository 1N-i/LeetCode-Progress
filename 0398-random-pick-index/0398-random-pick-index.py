import random
class Solution(object):
    def __init__(self, nums):
        self.map = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in self.map:
                self.map[num] = []

            self.map[num].append(i)

        
    def pick(self, target):
        return random.choice(self.map[target])