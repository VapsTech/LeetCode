#VapsTech | 08/08/2024
#Complexity: O(n)
#Runtime:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        duplicates = [-101] * n 

        idx = 0
        for i in range(n):
            if nums[i] not in duplicates:
                #add the different num to duplicate and remove duplication in nums
                nums[idx] = duplicates[idx] = nums[i] 
                #Move on to next changing idx
                idx += 1 

        return idx #number of different numbers
        