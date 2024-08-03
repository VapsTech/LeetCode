#VapsTech | 01/08/2024
#Complexity: O(n)
#Runtime: 42ms | Beats 80%
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { 'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000 }
        num = 0
        size = len(s)

        for i in range(size): #iterate from 0 to last char index
            if (i < size-1) and roman[s[i]] < roman[s[i+1]]: #if it is not the last index & value is less than the next char value
                num -= roman[s[i]] #subtract 
            else:
                num += roman[s[i]] #add 

        return num

