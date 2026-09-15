class Solution:
    def frequencySort(self, s: str) -> str:
        map_s = {}

        for l in s:
            if l not in map_s: map_s[l] = 0
            map_s[l] += 1

        sorted_map = sorted(map_s.items(), key=lambda item: item[1], reverse=True)

        ans = ""
        for l, qtd in sorted_map:
            ans += l * qtd

        return ans