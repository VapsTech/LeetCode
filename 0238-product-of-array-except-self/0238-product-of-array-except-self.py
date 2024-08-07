#VapsTech && Alef-Keuffer | 08/07/2024
#Complexity: O(n)
#Runtime: 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [1] * n
        suf = [1] * n
        ans = [1] * n

        #Prefix Array
        mult = 1
        for i in range(1,n):
            mult *= nums[i-1] #multiplying from first index to second last index
            pre[i] = mult
        pre[0] = 1 #First index equal to 1


        #Sufix Array
        mult = 1
        for i in range(n-1):
            mult *= nums[n-1-i] #Multiplying from last index to first
            suf[i+1] = mult #Start from second index
        suf[0] = 1 #First index equal to be last index equal 1 when reversed
        suf = list(reversed(suf))

        #Multiply prefix with sufix:   
        for i in range(n):
            ans[i] = suf[i] * pre[i]

        return ans
        