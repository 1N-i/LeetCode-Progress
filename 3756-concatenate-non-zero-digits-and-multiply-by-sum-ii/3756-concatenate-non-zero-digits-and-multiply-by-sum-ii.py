class Solution(object):
    def sumAndMultiply(self, s, queries):
        prefix_sum, prefix_val, prefix_count = [0], [0], [0]

        for i in range(len(s)):
            if s[i] != "0":
                prefix_val.append((prefix_val[i] * 10 + int(s[i])) % ((10 ** 9) + 7))
                prefix_count.append(prefix_count[-1] + 1)
            else:
                prefix_val.append(prefix_val[-1])
                prefix_count.append(prefix_count[-1])

            prefix_sum.append(prefix_sum[i] + int(s[i]))

        ans = []
        mod = 10 ** 9 + 7
        for start, end in queries:
            querie_sum = prefix_sum[end + 1] - prefix_sum[start]
            m = prefix_count[end + 1] - prefix_count[start]
            querie_x = (prefix_val[end + 1] - prefix_val[start] * pow(10, m, mod)) % mod
            ans.append((querie_sum * querie_x) % mod)

        return ans