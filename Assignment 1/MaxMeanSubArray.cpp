//technique: Fixed-size sliding window
//time complexity = O(n)
//space complexity = O(n)

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    double maxMeanSubArray(vector<int> nums, int subSize) {
                
        int maxSum = 0;
        int currSum = 0;
        
        //find max mean sum of first window
        for (int i = 0; i < subSize; i++){
            maxSum += nums[i];
        }

        //find sums of remaining windows
        //if a window > max, update
        currSum = maxSum;

        for (int i = subSize; i < nums.size(); i++){
            currSum += nums[i] - nums[i - subSize];
            maxSum = max(maxSum, currSum);
        }

        return (double)maxSum / subSize;
    }
        
};

int main(){

    Solution solution;

    vector<int> test{4, 5, -3, 2, 6, 1};
    cout << "test 1: " << solution.maxMeanSubArray(test, 2) << endl;
    
    cout << "test 2: " << solution.maxMeanSubArray(test, 3) << endl;
    
	test = {1, 1, 1, 1, -1, -1, 2, -1, -1};
    cout << "test 3: " << solution.maxMeanSubArray(test, 3) << endl;

	test = {1, 1, 1, 1, -1, -1, 2, -1, -1, 6};
    cout << "test 4: " << solution.maxMeanSubArray(test, 5) << endl;

    return 0;

}

//time spent on problem: 30 min