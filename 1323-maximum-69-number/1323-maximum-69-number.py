class Solution(object):
    def maximum69Number (self, num):
        list_num = list(str(num))
        if "6" not in list_num: return num
        
        for i in range(len(list_num)):
            if list_num[i] == "6":
                list_num[i] = "9"
                return int("".join(list_num))