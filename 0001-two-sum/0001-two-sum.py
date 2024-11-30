#VapsTech | 11/29/2024
#Complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        nums_dic = {}
        for index in range(len(nums)):
            nums_dic[nums[index]] = index

        for index in range(len(nums)):
            value = target - nums[index]

            if value in nums_dic and nums_dic[value] != index:
                return [index, nums_dic[value]] 

   
