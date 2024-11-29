#VapsTech | 11/29/2024
#Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        duplicates = set()
        for item in nums:
            if item in duplicates:
                return True
            else:
                duplicates.add(item)
        
        return False

        