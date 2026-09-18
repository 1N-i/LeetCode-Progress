class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        ans, map_ans = [], {}
        not_arr2 = []

        for num in arr1:
            if num not in map_ans:
                map_ans[num] = 0
            if num not in arr2:
                not_arr2.append(num)

            map_ans[num] += 1

        for num in arr2:
            ans.extend([num] * map_ans[num])

        not_arr2.sort()
        ans.extend(not_arr2)
        return ans