class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]

        permutations = self.permute(nums[1:])
        ans = []

        for p in permutations:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                ans.append(p_copy)

        return ans