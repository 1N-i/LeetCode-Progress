class Solution(object):
    def countCharacters(self, words, chars):
        chars_map = {}
        for l in chars:
            chars_map[l] = chars_map.get(l, 0) + 1

        ans = 0
        for word in words:
            word_map = {}
            for l in word:
                word_map[l] = word_map.get(l, 0) + 1

            can_form = True
            for l, count in word_map.items():
                if chars_map.get(l, 0) < count:
                    can_form = False
                    break

            if can_form:
                ans += len(word)

        return ans