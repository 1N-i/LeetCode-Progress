class Solution(object):
    def recoverOrder(self, order, friends):
        ans = []
        for friend in order:
            if friend in friends:
                ans.append(friend)

        return ans