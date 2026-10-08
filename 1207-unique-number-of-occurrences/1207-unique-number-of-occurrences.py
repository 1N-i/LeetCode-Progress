class Solution(object):
    def uniqueOccurrences(self, arr):
        guide = {}

        for num in arr:
            guide[num] = guide.get(num, 0) + 1

        seen = set()
        for num in guide:
            if guide[num] in seen:
                return False
            seen.add(guide[num])

        return True