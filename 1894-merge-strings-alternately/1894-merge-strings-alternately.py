#VapsTech | 08/06/2024
#Complexity: O(n)
#Runtime: 27ms | Beats 90%
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = 0
        mergeWord = []

        word1_len = len(word1)
        word2_len = len(word2)

        #Find max Length
        length = word1_len if word1_len > word2_len else word2_len

        for i in range(length):
            if (i < word1_len): #check if index is not out of range to append the char
                mergeWord.append(word1[i])
            if (i < word2_len): #check if index is not out of range to append the char
                mergeWord.append(word2[i])

        return ''.join(mergeWord) #turn list into a string

#Complexity: O(n)
        


                
