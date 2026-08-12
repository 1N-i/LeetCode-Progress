class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        ans = 0

        for hour in hours:
            if hour >= target: ans += 1

        return ans        