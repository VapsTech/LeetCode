#VapsTech
#Complexity: O(m*n)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        compare = []
        count = 0
        idx = 0

        while idx < len(haystack):
            
            if (haystack[idx] == needle[count]): #Check if char is same
                compare.append(haystack[idx])
                count += 1 #Increment needle's index
            else:
                if count > 0: 
                    idx = idx - count #Reset idx to one position after the attempted needle
                #Reset compare list & needle's index
                count = 0
                compare = []


            if (len(compare) == len(needle)): #Check if we found all chars from needle
                return idx + 1 - len(needle) #Return the first idx position the needle
        
            idx += 1

        return -1
        