#VapsTech | 11/29/2024
#Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_dic = {}
        t_dic = {}
        for index in range(len(s)):
            if s[index] in s_dic:
                s_dic[s[index]] += 1
            else:
                s_dic[s[index]] = 1
            if t[index] in t_dic:
                t_dic[t[index]] += 1
            else:
                t_dic[t[index]] = 1

        return s_dic == t_dic

        #for char in s:
        #    if (char not in t_dic) or (s_dic[char] - t_dic[char] != 0):
        #        return False

        #return True  
                
        
        