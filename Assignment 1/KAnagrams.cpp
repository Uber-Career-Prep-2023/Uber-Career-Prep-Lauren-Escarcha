//technique: Sort the array, then solve
//time complexity = O(n)
//space complexity = O(n)

#include <map>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    bool KAnagrams(string first, string second, int maxDiff) {

        map<char, int> firstCount;
        map<char, int> secondCount;
        int diffSum = 0;

        //base case
        if(first.size() != second.size()){
            cout << "False";
            return false;
        }

        //add to respective maps
        for(int i = 0; i < first.size(); i++){
            if(firstCount.find(first[i]) == firstCount.end())
            {
                firstCount.insert({first[i], 1});
            } 
            else if (firstCount.find(first[i]) != firstCount.end())
            {
                firstCount[first[i]]++;
            }

            if(secondCount.find(second[i]) == secondCount.end())
            {
                secondCount.insert({second[i], 1});
            } 
            else if (secondCount.find(second[i]) != secondCount.end())
            {
                secondCount[second[i]]++;
            }
        }

        //compare respective maps
        map<char, int>:: iterator it;
        if(firstCount.size() > secondCount.size()){
            for (it = firstCount.begin(); it != firstCount.end(); it++)
            {
                if(secondCount.find(it->first) != secondCount.end())
                {
                    //if char is found in second count's map
                    //check for diff
                    int currDiff = it->second - secondCount[it->first];
                    if(currDiff > 0){
                        diffSum += currDiff;
                    }
                }
                else {
                    //char in first is not found in second
                    //so add all difference
                    diffSum += it->second;
                }
            }
        } else {
            for (it = secondCount.begin(); it != secondCount.end(); it++)
            {
                if(firstCount.find(it->first) != firstCount.end())
                {
                    //if char is found in firstCount's map
                    //check for diff
                    int currDiff = it->second - firstCount[it->first];
                    if(currDiff > 0){
                        diffSum += currDiff;
                    }

                    // cout << it->first << " " << diffSum << endl;;
                }
                else {
                    //char in second is not found in first
                    //so add all difference
                    diffSum += it->second;
                    // cout << it->first << " " << diffSum << endl;;
                }
            }
        }

        if(diffSum > maxDiff){
            cout << "False";
            return false;
        }

        //else
        cout << "True";
        return true;
    }
        
};

int main(){

    Solution solution;

    solution.KAnagrams("apple", "peach", 1);
    cout << "\n";
    solution.KAnagrams("apple", "peach", 2);
    cout << "\n";
    solution.KAnagrams("cat", "dog", 3);
    cout << "\n";
    solution.KAnagrams("debit curd", "bad credit", 1);
    cout << "\n";
    solution.KAnagrams("baseball", "basketball", 2);
    cout << "\n";

    return 0;

}

//time spent on problem: 30 min
