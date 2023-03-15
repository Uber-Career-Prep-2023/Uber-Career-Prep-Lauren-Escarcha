//technique: Sort the array, then solve
//time complexity = O(n)
//space complexity = O(n)

#include <vector>
#include <bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<int>> MergeIntervals(vector<vector<int>> intervals) {

        //sort
        sort(intervals.begin(), intervals.end());

        //final vactor
        vector<vector<int>> merged;

        //iterate thru intervals 
        for(auto interval : intervals){
            //if final is empty
            //or last index of last interval < first index of curr interval
            if(merged.empty() || merged.back()[1] < interval[0]){
                merged.push_back(interval);
            }
            else{
                merged.back()[1] = max(merged.back()[1], interval[1]);
            }
        }
        return merged;
    }



        
        
};

int main(){

    Solution solution;

    vector<vector<int>> test = solution.MergeIntervals({{2, 3}, {4, 8}, {1, 2}, {5, 7}, {9, 12}});
    for(int i = 0; i < test.size(); i++){
        cout << "(" << test[i][0] << ", " << test[i][1] << ") ";
    }
    cout << endl;

    return 0;

}

//time spent on problem: 30 min
