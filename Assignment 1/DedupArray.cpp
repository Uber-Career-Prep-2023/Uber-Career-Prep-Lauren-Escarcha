//technique: One-directional running computation/total
//time complexity = O(n)
//space complexity = O(n)

#include <vector>
#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    set<int> DedupArray(vector<int> input) {

        set<int> output;

        for(int i = 0; i < input.size(); i++){
            output.insert(input[i]);
        }

        return output;
    }



        
        
};

int main(){

    Solution solution;
    set<int>::iterator it;

    set<int> test = solution.DedupArray({1, 2, 2, 3, 3, 3, 4, 4, 4, 4});
    for(it = test.begin(); it != test.end(); it++){
        cout << *it << ", ";
    }
    cout << endl;

    test = solution.DedupArray({0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15});
    for(it = test.begin(); it != test.end(); it++){
        cout << *it << ", ";
    }
    cout << endl;

    test = solution.DedupArray({1, 3, 4, 8, 10, 12});
    for(it = test.begin(); it != test.end(); it++){
        cout << *it << ", ";
    }
    cout << endl;

    return 0;

}

//time spent on problem: 15 min
