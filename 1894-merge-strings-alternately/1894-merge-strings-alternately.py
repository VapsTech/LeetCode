#VapsTech | 08/06/2024
#Complexity: O(n)
#Runtime: 30ms | Beats 85%
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = 0
        mergeWord = []

        length = max(len(word1), len(word2)) #find longest string

        for i in range(length):
            if (i < len(word1)): #check if index is not out of range to append the char
                mergeWord.append(word1[i])
            if (i < len(word2)): #check if index is not out of range to append the char
                mergeWord.append(word2[i])

        return ''.join(mergeWord) #turn list into a string

#Complexity: O(n)
        


                
