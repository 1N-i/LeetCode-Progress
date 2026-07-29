class Solution(object):
    def isAnagram(self, s, t):
        list = []
        for letter in s:
            list.append(letter)
        list.sort()
        lists = list

        list = []
        for letter in t:
            list.append(letter)
        list.sort()
        listt = list

        return lists == listt