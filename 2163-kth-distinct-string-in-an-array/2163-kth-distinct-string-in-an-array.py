#VapsTech | 08/05/2024
#Complexity: O(n)
#Runtime:
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = len(arr)
        n_set = len(set(arr))        
        
        if n == 1:
            return arr[0]

        if n_set == 1: #Empty(0) or arr of only one element(1)
            return ""

        if n_set == n:
            return arr[k-1]
            
        arr_ans = []
        for char in arr:
            if arr.count(char) == 1: #counter to check frequency 
                arr_ans.append(char) #Arrange the arr w/ no duplicates

        if k <= len(arr_ans): #check if k is inside range
            return arr_ans[k-1]
        else:
            return ""

        duplicate = {}
        for char in arr:
            if char not in duplicate:
                duplicate.append(char)
                duplicate[char] = arr.count(char) 
