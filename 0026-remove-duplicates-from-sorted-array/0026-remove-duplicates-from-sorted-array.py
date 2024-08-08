class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        duplicates = [-101] * n 

        idx = 0
        for i in range(n):
            if nums[i] not in duplicates:
                nums[idx] = duplicates[idx] = nums[i] #Add single num to duplicate
                
                idx += 1 #Move to next changing idx

        return idx
        