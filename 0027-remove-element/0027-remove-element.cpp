//VapsTech | 08/07/2024
//Complexity: O(n)
//Runtime: 0ms | Beats 100%
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int count{0};

        for (int i = 0; i < n; i++){
            if (nums[i] != val){
                nums[count] = nums[i];
                count++;
            }
        }

        return count;
    }
};