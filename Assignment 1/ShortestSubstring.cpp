//technique: Two arrays/strings two-pointer (brute force teehee)
//time complexity = O(3n) => O(n)
//space complexity = O(n)

#include <string>
#include <map>
#include<bits/stdc++.h>
#include <iostream>
using namespace std;

class Solution {
public:
    int ShortestSubstring(string input, string sub) {

        //map for sub
        map<char, int> charCount; 
        //map for input
        map<char, pair<int, queue<int>>> trackInput; //pair = <count, queue of indexes wher char is found>

        int maxInd = 0;
        int minInd = input.size()-1;

        //make all lowercase since case insensitive
        transform(input.begin(), input.end(), input.begin(), ::tolower);

       //iterate thru SUB and store counts in map
        for(int i = 0; i < sub.size(); i++){

            char currChar = tolower(sub[i]);

            //if first time finding
            if(charCount.find(currChar) == charCount.end()){
                charCount.insert({currChar, 1});
            } else if(charCount.find(currChar) != charCount.end()){
                //already added, increment count
                charCount[currChar]++;
            }
        
        }

        //iterate thru INPUT and check counts in map
        for(int i = 0; i < input.size(); i++){

            char currChar = tolower(input[i]);

            //if char in input is in sub
            if(charCount.find(currChar) != charCount.end()){

                //add in trackInput, if not added yet
                if(trackInput.find(currChar) == trackInput.end()){
                    //make queue
                    queue<int> q;
                    q.push(i);
                    //make pair
                    pair<int, queue<int>> charPair(1, q);
                    //insert in map
                    trackInput.insert({currChar, charPair});
                } else {
                    //else, already added

                    //increment count
                    trackInput[currChar].first++;
                    //add index to vector
                    trackInput[currChar].second.push(i);

                    //check if sub can be shortened
                    if(trackInput[currChar].first > charCount[currChar]){
                        //removes the earliest index of where the char was found

                        trackInput[currChar].second.pop();
                        
                        trackInput[currChar].first--;
                    }
                }
                //else, disregard char

            }
        
        }

        //find length 
        map<char, pair<int, queue<int>>>::iterator it;
        for (it = trackInput.begin(); it != trackInput.end(); it++)
                {
                    //min is lowest head of queue
                    //max is greatest back of queue
                    minInd = min(minInd, it->second.second.front());
                    maxInd = max(maxInd, it->second.second.back());

                    //just realized I didn't need a queue, but could have just stored as another pair for <min, max> indexes found but oh well
        }
    
        return maxInd - minInd;
    }
        
};

int main(){

    Solution solution;

    cout << solution.ShortestSubstring("abracadabra", "abc");
    
    return 0;

}

//time spent on problem: 40+ min
//went overtime :')