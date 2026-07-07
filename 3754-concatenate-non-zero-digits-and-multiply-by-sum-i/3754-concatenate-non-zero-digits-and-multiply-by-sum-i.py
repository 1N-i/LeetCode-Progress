class Solution(object):
    def sumAndMultiply(self, n):
        n_string = ""
        for num in str(n):
            if num != "0":
                n_string += num

        if n_string == "": n_string = "0"

        n_list = list(n_string)
        for i in range(len(n_list)):
            n_list[i] = int(n_list[i])

        return sum(n_list) * int(n_string)