class Solution(object):
    def reverseStr(self, s, k):
        lista_s = list(s)
        
        for i in range(0, len(s), 2 * k):
            lista_s[i : i + k] = lista_s[i : i + k][::-1]
            
        return "".join(lista_s)