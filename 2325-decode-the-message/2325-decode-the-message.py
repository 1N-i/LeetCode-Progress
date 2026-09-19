import string
class Solution(object):
    def decodeMessage(self, key, message):
        ans, guide = [], {}
        alphabet = string.ascii_lowercase
        letters = 0

        for l in key:
            if l == " ": continue
            if l not in guide:
                guide[l] = alphabet[letters]
                letters += 1

            if letters == 26: break

        for l in message:
            if l == " ":
                ans.append(" ")
                continue
            ans.append(guide[l])

        return "".join(ans)