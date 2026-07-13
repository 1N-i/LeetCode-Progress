class Solution(object):
    def flipAndInvertImage(self, image):
        ans = []
        
        for im in image:
            temp_im = im[::-1]
            for num in range(len(temp_im)):
                if temp_im[num] == 1: temp_im[num] = 0
                else: temp_im[num] = 1

            ans.append(temp_im)

        return ans