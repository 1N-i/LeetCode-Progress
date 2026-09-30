class Solution(object):
    def largestAltitude(self, gain):
        ans = [0]
        altitude = 0

        for num in gain:
            altitude += num
            ans.append(altitude)

        return max(ans)