#VapsTech | 11/29/2024
#Complexity: O(n+m)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False

        #Make Dictionary of Magazine with count
        mag_dic = {}
        for char in magazine:
            if char in mag_dic:
                mag_dic[char] += 1
            else:
                mag_dic[char] = 1

        #Make Dictionary of RansomNote with count
        ran_dic = {}
        for char in ransomNote:
            if char in ran_dic:
                ran_dic[char] += 1
            else:
                ran_dic[char] = 1

        for char in ran_dic:
            #Check if char exists in mag, then check if there are enough chars in mag to make ran
            if char not in mag_dic or (mag_dic[char] - ran_dic[char]) < 0:
                return False
        
        return True
            

        