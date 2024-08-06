//VapsTech | 08/06/2024
//Complexity: O(n)
//Runtime: 
#include <cmath>
class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int n = nums.size();

        vector<int> pos;
        vector<int> neg;
        int closest;
 
        //Create the list with positive nums and list with neg nums
        for (int i = 0; i < n; ++i){
            if (nums[i] == 0){
                return 0;
            }
            if (nums[i] > 0){
                pos.push_back(nums[i]);

            } else {
                neg.push_back(nums[i]);
            }
        }

        //Find smallest in positive list
        int closest_pos = pow(10,5);
        for (int i = 0; i < pos.size(); ++i){
            if (pos[i] < closest_pos){
                closest_pos = pos[i];
            }
        }

        //Find greatest (closest to zero) in negative list 
        int closest_neg = pow(-10,5);
        for (int i = 0; i < neg.size(); ++i){
            if (neg[i] > closest_neg){
                closest_neg = neg[i];
            }
        }

        if (pos.empty()){
            return closest_neg;
        }
        else if (neg.empty()){
            return closest_pos;
        }

        //Check smallest between smallest positive list and smallest negative list
        if (closest_pos <= abs(closest_neg)){
            return closest_pos;
        } else {
            return closest_neg;
        }
    }
};