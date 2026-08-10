class Solution(object):
    def bulbSwitch(self, n):
        """ Main logic to reach the math conclusion
        ans = [True] * n

        for Round in range(2, n + 1):
            for i in range(Round - 1, n, Round):
                ans[i] = not ans[i]

        return sum(ans)
        """

        return int(n ** 0.5)