//technique: Variable-size (shrinking/growing) sliding window
//time complexity = O(n)
//space complexity = O(n)

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int ZeroSumSubArrays(vector<int> nums) {
                
        //initialize sum to the first index of the array
        int sum = nums[0];
        int zeroSumCount = 0;
        
        for(int i = 0; i < nums.size(); i++){
            
            //if the prefix is != 0
            //restart the x
            if(sum != 0){
                sum = -1; 
            }
            
            sum += nums[i];
            
            //check to see if subarray == 0
            if(sum == 0){
                zeroSumCount++;
            }
            
        }
        
        return zeroSumCount;
    }
        
};

int main(){

    Solution solution;

    vector<int> test{4, 5, 2, -1, -3, -3, 4, 6, -7};
    cout << "test 1: " << solution.ZeroSumSubArrays(test) << endl;
    
    test = {1, 8, 7, 3, 11, 9};
    cout << "test 2: " << solution.ZeroSumSubArrays(test) << endl;
    
	test = {8, -5, 0, -2, 3, -4};
    cout << "test 3: " << solution.ZeroSumSubArrays(test) << endl;

	// test = {1, 1, 1, 1, -1, -1, 2, -1, -1, 6};
    // cout << "test 4: " << solution.ZeroSumSubArrays(test, 5) << endl;

    return 0;

}

//time spent on problem: 30 min