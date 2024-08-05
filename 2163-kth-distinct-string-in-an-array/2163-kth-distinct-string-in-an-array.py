#VapsTech | 08/05/2024
#Complexity: O(n)
#Runtime:
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        if len(arr) == 1:
            return arr[0]

        #Empty(0) or arr of only one element(1)
        if arr.count(arr[0]) == len(arr) or len(set(arr)) < 2:
            return ""
 
        arr_ans = []
        for char in arr:
            if arr.count(char) == 1: #counter to check frequency 
                arr_ans.append(char) #Arrange the arr w/ no duplicates

        if arr_ans == []: #check if there are only duplicates  
            return arr[k-1]

        if k <= len(arr_ans): #check if k is inside range
            return arr_ans[k-1]
        else:
            return ""