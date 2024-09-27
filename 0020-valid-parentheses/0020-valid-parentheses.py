#VapsTech
#Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:

        values = {"(":")" , "[":"]" , "{":"}" } 

        valid_closing = []

        for char in s:
            if char in values: #Check if it is a opening
                valid_closing.append(values[char]) #Append to the Stack
                continue 
            
            if char not in valid_closing or char != valid_closing.pop(): #Pop the Stack 
                return False
            
        return not valid_closing
                
    

        