#VapsTech
#Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:

        opening = ("(", "[", "{")
        closing = {"(":")" , "[":"]" , "{":"}" }

        valid_closing = []

        if s[0] not in opening:
            return False

        for char in s:
            if char in opening: #Check if it is a opening
                valid_closing.append(closing[char]) #Append to the Stack
                continue 
            
            if char not in valid_closing or char != valid_closing.pop(): #Pop the Stack 
                return False
            
        return not valid_closing
                
    

        