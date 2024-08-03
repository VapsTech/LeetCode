#VapsTech | 08/03/2024
#Complexity: O(n*log(n))
#Runtime: 66ms | Beats 90%
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #Sort the two lists
        target.sort()
        arr.sort()

        #Check if they are equal
        return True if arr == target else False
            

            