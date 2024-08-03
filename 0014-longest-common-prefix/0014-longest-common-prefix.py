#VapsTech | 08/03/2024
#Complexity: O(n^2)
#Runtime: 32ms | Beats 88%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs: #if there is an empty string in the list
            return ''

        size_strs = len(strs)

        prefix = strs[0] 
        for i in range(1, size_strs): #run from second string to last string                     
            for j in range(len(prefix)): 
                if j >= len(strs[i]) or prefix[j] != strs[i][j]: #if its index is out of the string or have different chars
                    prefix = prefix[:j] #Cuts the prefix up until same char or length 
                    break #exits the inner loop to check the next string
 
        return ''.join(prefix)

        