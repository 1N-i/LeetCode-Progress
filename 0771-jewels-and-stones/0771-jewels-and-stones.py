class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        is_jewel = 0
        jewels, stones = list(jewels), list(stones)
        for stone in stones:
            if stone in jewels:
                is_jewel += 1

        return is_jewel