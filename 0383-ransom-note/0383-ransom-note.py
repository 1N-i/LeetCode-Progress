class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransom_map, magazine_map = {}, {}

        for l in ransomNote:
            ransom_map[l] = ransom_map.get(l, 0) + 1
        for l in magazine:
            magazine_map[l] = magazine_map.get(l, 0) + 1

        for l in ransom_map:
            if magazine_map.get(l, 0) == 0 or ransom_map[l] > magazine_map[l]:
                return False

        return True