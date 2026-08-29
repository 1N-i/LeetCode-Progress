class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = []
        for word in words:
            count = 0
            for letter in word:
                count += weights[ord(letter) - 97] #97 = ord("a")
            ans.append(chr(97 + (25 - (count % 26))))

        return "".join(ans)