class Solution(object):
    def maxScore(self, cardPoints, k):
        maxSum = sum(cardPoints[:k])
        left, right = k -1, len(cardPoints) - 1
        tempSum = maxSum

        for i in range(k):
            tempSum = tempSum - cardPoints[left] + cardPoints[right]
            maxSum = max(maxSum, tempSum)
            left -= 1
            right -= 1

        return maxSum