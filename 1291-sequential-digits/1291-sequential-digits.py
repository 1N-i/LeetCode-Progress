list_nums = list(range(1, 10))

class Solution(object):
    def getListOfCertainSize(self, maximunRage, low, high):
        temp_ans = []
        for i in range(10 - maximunRage):
            single_int = int("".join(map(str, list_nums[i:i + maximunRage])))
            if low <= single_int <= high:
                temp_ans.append(single_int)

        return temp_ans

    def sequentialDigits(self, low, high):
        len_low = len(str(low))
        len_high = len(str(high))
        ans = []

        for i in range(len_low, len_high + 1):
            temp_ans = self.getListOfCertainSize(i, low, high)
            ans.extend(temp_ans)

        return ans