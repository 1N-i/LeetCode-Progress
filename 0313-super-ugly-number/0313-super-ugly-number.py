class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ans = [1]
        p = [0] * len(primes)

        while len(ans) < n:
            opt_ = [ans[p[i]] * primes[i] for i in range(len(primes))]
            to_add = min(opt_)
            ans.append(to_add)

            for i in range(len(opt_)):
                if opt_[i] == to_add: p[i] += 1

        return ans[-1]