#VapsTech | 08/04/2024
#Complexity: O(n)
#Runtime: 116ms | Beats 80%
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        n = len(nums)
        
        for i in range(n): #iterate from index 0 to last index
            if (abs(nums[i]) < abs(closest)) or (abs(nums[i]) == abs(closest) and nums[i] > closest): 
                closest = nums[i]

        return closest
        