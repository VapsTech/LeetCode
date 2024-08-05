#VapsTech | 08/05/2024
#Complexity: O(n)
#Runtime:
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        idx = k - 1

        # address edge case that
        # `k`` is so big that it's
        # out of bounds even for
        # the original array
        if idx >= len(arr):
            return ""

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

        return duplicates[k-1]

        # n = len(arr)
        # if n == 1:
        #     return arr[0]

        # n_set = len(set(arr))
        # if n_set == 1: #Empty(0) or arr of only one element(1)
        #     return ""

        # if n_set == n:
        #     return arr[k-1]
            
        # arr_ans = []
        # for char in arr:
        #     if arr.count(char) == 1: #counter to check frequency 
        #         arr_ans.append(char) #Arrange the arr w/ no duplicates

        # if k <= len(arr_ans): #check if k is inside range
        #     return arr_ans[k-1]
        # else:
        #     return ""