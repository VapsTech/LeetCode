#VapsTech && Alef-Keuffer| 08/05/2024
#Complexity: O(n)
#Runtime: 60ms | Beats 90%
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        idx = k - 1
        # address edge case that
        # `k`` is so big that it's
        # out of bounds even for
        # the original array
        if idx >= len(arr):
            return ""

        #Create hashset of duplicates -> key : num / value : count
        duplicate = {}
        for char in arr:
            if char not in duplicate:
                duplicate[char] = 0
            duplicate[char] += 1

        # early return id33: case no duplicates
        # addresses Example 2
        if len(duplicate) == len(arr):
            return arr[idx]

        # we know there are duplicates because
        # of early return id33 and
        duplicates = [char for char in duplicate if duplicate[char] == 1]

        # addresses Example 3
        if idx >= len(duplicates):
            return ""      

        return duplicates[idx]
