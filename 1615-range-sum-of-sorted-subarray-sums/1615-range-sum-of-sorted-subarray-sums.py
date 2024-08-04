#VapsTech | 08/04/2024
#Complexity: O(n^2*log(n))
#Runtime: 200ms | Beats 90%
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        modulo = pow(10,9)+7
        arr_sum = []
        summ = 0

        for i in range(n):
            summ = 0 #Reset Summ
            for j in range(i,n): 
                summ += nums[j] #Sum all possible numbers using j index
                arr_sum.append(summ) #Append the summ to the array
        
        #sort the array
        arr_sum.sort()
    
        #return the sum from left index to right index
        return sum(arr_sum[left-1:right]) % modulo
