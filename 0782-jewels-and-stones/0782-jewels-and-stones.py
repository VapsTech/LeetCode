#VapsTech | 11/28/2024
#Complexity: O(n+m) 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        jewels_set = set(jewels)

        for stone_index in range(len(stones)):
            if stones[stone_index] in jewels_set: #Access jewels in O(1)
                count += 1            
        
        return count
        