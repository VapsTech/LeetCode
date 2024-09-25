#VapsTech | 09/24/2024
#Complexity: O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x) #Turn into a str object
        x_reversed = ''.join(reversed(x)) #Join from right to left 

        return x == x_reversed
        