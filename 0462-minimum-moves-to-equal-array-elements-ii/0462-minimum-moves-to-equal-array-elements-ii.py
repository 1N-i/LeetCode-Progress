class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        len_nums = len(nums)
        
        if len_nums % 2 != 0:
            mediana_id = int((len_nums / 2) + 0.5)
            mediana = nums[mediana_id - 1]
        else:
            mediana_id = int(len(nums) / 2)
            mediana = (nums[mediana_id - 1] + nums[mediana_id]) / 2

        ans = 0
        for num in nums:
            ans += abs(num - mediana)
        return int(ans)