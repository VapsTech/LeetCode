#VapsTech | 08/08/2024
#Complexity: O(n)
#Runtime: 34ms | Beats 70%
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_size = len(s)
        t_size = len(t)
        s_index = t_index = 0

        while t_index < t_size and s_index < s_size: #run until index is out of range for any of the strs
            if (s[s_index] == t[t_index]): #check if s char is in some t index
                s_index += 1
            t_index += 1
        
        return s_index == s_size
            

