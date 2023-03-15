//technique: Sort the array, then solve
//time complexity = O(n)
//space complexity = O(n)

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int MissingInteger(vector<int> nums, int missing) {

        for(int i = 1; i < missing; i++){
            if(i != nums[i - 1]){
                return i;
            } else if((i == nums.size()) && nums[nums.size() - 1] != missing){
                //if missing num is at the end
                return missing;
            }
        }

        return -1;
    }
        
};

int main(){

    Solution solution;

    //returns -1 if missingNum is not there

    vector<int> input{1, 2, 3, 4, 6, 7};
    cout << "test 1: " << solution.MissingInteger(input, 7) << endl;
    
    input = {1};
    cout << "test 2: " << solution.MissingInteger(input, 2) << endl;
    
    input = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12};
    cout << "test 3: " << solution.MissingInteger(input, 12) << endl;
    
    input = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
    cout << "test 4: " << solution.MissingInteger(input, 12) << endl;
    
    return 0;

}

//time spent on problem: 15 min
