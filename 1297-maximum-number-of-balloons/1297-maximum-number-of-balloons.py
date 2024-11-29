#VapsTech | 11/29/2024
#Complexity: O(n)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon = "balloon" 

        #Make counter of text
        text_dic = {}
        for char in text:
            if char in text_dic:
                text_dic[char] += 1
            else:
                text_dic[char] = 1

        #Find minimum number of balloon in text
        minimum = float('inf')
        for char in balloon:
            if char not in text_dic: 
                return 0
            
            if char == 'l' or char == 'o':
                if text_dic[char] < 2:
                    return 0
                else:
                    if text_dic[char] // 2 < minimum:
                        minimum = text_dic[char] // 2
            else:
                if text_dic[char] < minimum:
                    minimum = text_dic[char] 

        return minimum
