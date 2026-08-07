class Solution(object):
    def nthUglyNumber(self, n):
        ans = [1]
        p2, p3, p5 = 0, 0, 0

        while len(ans) < n:
            opt2 = ans[p2] * 2
            opt3 = ans[p3] * 3
            opt5 = ans[p5] * 5

            to_add = min(opt2, opt3, opt5)
            ans.append(to_add)

            if to_add == opt2: p2 += 1
            if to_add == opt3: p3 += 1
            if to_add == opt5: p5 += 1

        return ans[-1]