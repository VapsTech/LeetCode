//VapsTech | 08/06/2024
//Complexity: O(n)
//Runtime: 
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.length();
        int n2 = word2.length();

        //Get max size
        int size;
        if (n1 > n2){
            size = n1;
        } else {
            size = n2;
        }

        string ans_arr;

        for (int i = 0; i < size; ++i){
            if (i < n1) {
                ans_arr.push_back(word1[i]); //Append first if it's in range
            }
            if (i < n2) { 
                ans_arr.push_back(word2[i]); //Append second if it's in range
            }
        }

        return ans_arr;
        
    }
};