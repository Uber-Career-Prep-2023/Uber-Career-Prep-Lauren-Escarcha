//technique: Two arrays/strings two-pointer (brute force teehee)
//time complexity = O(3n) => O(n)
//space complexity = O(n)

#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    void BackspaceStringCompare(string input1, string input2) {

        //count for original string
        int backspaceCount = 0;
        string final1 = "";
        string final2 = "";

        //for first input
        for(int k = input1.size() - 1; k >= 0; k--){

            if(input1[k] == '#'){
                //update # count
                //don't add to finalize string
                backspaceCount++;
            } 
            else if(backspaceCount > 0 && input1[k] != '#'){
                //letter after backspace is found
                //skip corresponding letters before the #
                backspaceCount--;
            } else {
                // just add to finalized string
                final1 += input1[k];
            }
        }
        
        //  cout << final1 << " ";

        //for second input
        backspaceCount = 0;

        //for first input
        for(int k = input2.size() - 1; k >= 0; k--){
            if(input2[k] == '#'){
                //update # count
                //don't add to finalize string
                backspaceCount++;
            } 
            else if(backspaceCount > 0 && input2[k] != '#'){
                //letter after backspace is found
                //skip corresponding letters before the #
                backspaceCount--;
            } else {
                // just add to finalized string
                final2 += input2[k];
            }
        }

        // cout << final2 << endl;

        if(final1 == final2){
            cout << "True";
            return;
        }

        //else
        cout << "False";
    
    }
        
};

int main(){

    Solution solution;

    //true
    solution.BackspaceStringCompare("abcde", "abcde");
    cout << ": abcde, abcde";
    cout << "\n";

    //true
    solution.BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep");
    cout << ": Uber Career Prep, u#Uber Careee#r Prep";
    cout << "\n";


    //true
    solution.BackspaceStringCompare("abcw#xyz", "abcdef###xyz");
    cout << ": abcdef###xyz, abcw#xyz";
    cout << "\n";

    //false
    solution.BackspaceStringCompare("abcdef###xyz", "abcdefxyz###");
    cout << ": abcdef###xyz, abcdefxyz###";
    cout << "\n";

    //true
    solution.BackspaceStringCompare("uu##urmo#o#om", "urmom");
    cout << ": uu##urmo#o#om, urmom";
    cout << "\n";

    //true
    solution.BackspaceStringCompare("uu###urmo#o#om", "urmom");
    cout << ": uu###urmo#o#om, urmom";
    cout << "\n";
    
    return 0;

}

//time spent on problem: 40+ min
//went overtime sorry :')