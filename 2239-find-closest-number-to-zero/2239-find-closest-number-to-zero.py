class Solution(object):
    def findClosestNumber(self, nums):
        closest = nums[0]
        for num in nums:
            print(closest)
            if closest == -num:
                closest = abs(closest)

            elif closest > 0:
                if num > 0:
                    if num < closest:
                        closest = num
                else:
                    if -num < closest:
                        closest = num
            else:
                if num < 0:
                    if num > closest:
                        closest = num
                else:
                    if -num > closest:
                        closest = num

        return closest