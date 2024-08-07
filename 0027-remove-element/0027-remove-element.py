#VapsTech | 08/07/2024
#Complexity: O(n)
#Runtime:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) #Get total length 

        count = 0
        for item in nums:
            if item != val: #If it is not the val 
                nums[count] = item #Change nums without val
                count += 1 #Increment index

        return count #Return length of new arr without val