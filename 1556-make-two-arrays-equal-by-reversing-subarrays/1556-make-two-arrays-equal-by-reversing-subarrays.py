#VapsTech | 08/03/2024
#Complexity:
#Runtime: 
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        #Sort the two lists
        target.sort()
        arr.sort()

        #Check if they are equal
        return True if arr == target else False
            

            