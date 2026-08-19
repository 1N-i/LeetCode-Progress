class Solution:
    def singleNumber(self, nums):
        frequency_map = {}
        
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        ans = [num for num, count in frequency_map.items() if count == 1]
        
        return ans