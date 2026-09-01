class Solution(object):
    def maxScore(self, cardPoints, k):
        maxSum = sum(cardPoints[:k])
        left, right = k -1, len(cardPoints) - 1
        tempSum = maxSum

        for i in range(k):
            maxSum = max(maxSum, tempSum)
            tempSum = tempSum - cardPoints[left] + cardPoints[right]
            left -= 1
            right -= 1

        maxSum = max(maxSum, tempSum)
        return maxSum