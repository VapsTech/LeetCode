#VapsTech | 08/05/2024
#Complexity: 
#Runtime:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        str_list = []

        i = 0
        while i < n:
            start = i #start variable to begin new sequence
            while i+1 < n and nums[i] + 1 == nums[i+1]: #Check if int + 1 is equal to the next index
                i += 1 #increase the sequence
            if start != i: #If i has been incremented by any number 
                 str_list.append(f"{nums[start]}->{nums[i]}")
            else:    
                str_list.append(str(nums[i])) #Means i has not changed
            i += 1
        
        return str_list