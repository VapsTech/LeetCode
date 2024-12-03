#VapsTech | 12/03/2024
#Complexity: O(n)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left <= right:
            swap = s[left]
            s[left] = s[right]
            s[right] = swap

            left += 1
            right -= 1




        