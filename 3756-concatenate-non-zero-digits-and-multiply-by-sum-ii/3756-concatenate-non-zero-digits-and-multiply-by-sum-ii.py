class Solution(object):
    def sumAndMultiply(self, s, queries):
        size = len(s) + 1
        prefix_sum, prefix_val, prefix_count = [0] * size, [0] * size, [0] * size
        mod = 10 ** 9 + 7

        for i in range(len(s)):
            int_s_i = int(s[i])
            if s[i] != "0":
                prefix_val[i + 1] = (prefix_val[i] * 10 + int_s_i) % mod
                prefix_count[i + 1] = prefix_count[i] + 1
            else:
                prefix_val[i + 1] = prefix_val[i]
                prefix_count[i + 1] = prefix_count[i]

            prefix_sum[i + 1] = prefix_sum[i] + int_s_i

        ans = []
        for start, end in queries:
            querie_sum = prefix_sum[end + 1] - prefix_sum[start]
            m = prefix_count[end + 1] - prefix_count[start]
            querie_x = (prefix_val[end + 1] - prefix_val[start] * pow(10, m, mod)) % mod
            ans.append((querie_sum * querie_x) % mod)

        return ans