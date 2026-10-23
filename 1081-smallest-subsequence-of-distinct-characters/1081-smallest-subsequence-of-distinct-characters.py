class Solution:
    def smallestSubsequence(self, s: str) -> str:
        guide = {}
        for i in range(len(s)):
            if s[i] not in guide:
                guide[s[i]] = []
            guide[s[i]].append(i)

        ans = []
        visited = set()
        for i, l in enumerate(s):
            if l in visited:
                continue
                
            while ans and l < ans[-1] and guide[ans[-1]][-1] > i:
                removed = ans.pop()
                visited.remove(removed)

            ans.append(l)
            visited.add(l)

        return "".join(ans)