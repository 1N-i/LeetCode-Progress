class Solution(object):
    def isAnagram(self, s, t):
        def getList(word):
            list = []
            for letter in word:
                list.append(letter)
            list.sort()
            return list

        lists = getList(s)
        listt = getList(t)

        if lists == listt:
            return True
        else:
            return False