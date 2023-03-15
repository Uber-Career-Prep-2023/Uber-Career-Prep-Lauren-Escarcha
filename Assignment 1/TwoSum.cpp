//technique: One-directional running computation/total
//time complexity = O(n)
//space complexity = O(n)

#include <vector>
#include <map>
#include <iostream>
using namespace std;

class Solution {
public:
    int TwoSum(vector<int> nums, int target) {

        map<int, int> otherSum;
        //key will be difference
        //value will be index
        int pairCount = 0;

        for(int i = 0; i < nums.size(); i++){

            if(otherSum.find(nums[i]) != otherSum.end())
            {
                // its found
                // still store and update count
                pairCount += otherSum[nums[i]];
                // cout << "\n" << pairCount << " " << nums[i] << " " << target - nums[i] << endl;
                otherSum[nums[i]]++;

                otherSum.insert({target - nums[i], 1}); 

            } 
            else {
                //not found, need to add to map
                otherSum.insert({target - nums[i], 1}); 
                
            }
                    
        }

        return pairCount;
    }
};

int main(){

    Solution solution;
    
    cout << "test 1: " << 
    solution.TwoSum({1, 10, 8, 3, 2, 5, 7, 2, -2, -1}, 10) << endl;

    cout << "test 2: " << 
    solution.TwoSum({1, 10, 8, 3, 2, 5, 7, 2, -2, -1}, 9) << endl;

    cout << "test 3: " << 
    solution.TwoSum({4, 3, 3, 5, 7, 0, 2, 3, 8, 6}, 6) << endl;

    cout << "test 4: " << 
    solution.TwoSum({4, 3, 3, 5, 7, 0, 2, 3, 8, 6}, 1) << endl;

    return 0;

}

//time spent on problem: 15 min
