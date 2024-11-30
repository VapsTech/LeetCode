#VapsTech | 11/30/2024
#Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:  
        
        pal = []
        for char in s:
            if char.isalnum():
                pal.append(char.lower())

        n = len(pal)
        right = n - 1
        left = 0

        for i in range(n//2):
            if pal[left] != pal[right]:
                return False
            right -= 1
            left += 1
        
        return True