#VapsTech | 08/08/2024
#Complexity: O(n)
#Runtime: 85ms | Beats 20%
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)
        # duplicates = []

        # idx = 0
        # for i in range(n):
        #     if nums[i] not in duplicates:
        #         #add the different num to duplicate and remove duplication in nums
        #         duplicates.append(nums[i])
        #         nums[idx] = nums[i] 
        #         #Move on to next changing idx
        #         idx += 1 

        # return idx #number of different numbers

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
        