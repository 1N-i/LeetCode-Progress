class Solution(object):
    def areNumbersAscending(self, s):
        last_num = 0
        clean_s = s.split()

        for w in clean_s:
            if w.isdigit():
                if int(w) <= last_num:
                    return False
                else:
                    last_num = int(w)

        return True