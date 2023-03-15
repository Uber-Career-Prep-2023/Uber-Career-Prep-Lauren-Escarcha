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
        int indexHolder = 0;
        int backspaceCount = 0;
        string final1 = "";
        string final2 = "";

        //for first input
        for(int k = 0; k < input1.size(); k++){
            if(input1[k] == '#'){
                //update # count
                //don't add to finalize string
                backspaceCount++;
            } 
            else if(backspaceCount > 0 && input1[k] != '#'){
                //letter after backspace is found
                //delete corresponding letters before the #
                
                //final1 should have letter, if not, then its a stray #
                if(final1.empty()|| final1.size() < backspaceCount){
                    cout << "False";
                    return;
                }

                //(starting point, length)    
                final1.erase(final1.size() - (backspaceCount), (backspaceCount));
                //reset back count
                backspaceCount = 0;


                //be sure to actually add letter to string
                final1 += input1[k];
            } else {
                // just add to finalized string
                final1 += input1[k];
            }
        }
        
        //  cout << final1 << endl;

        //for second input
        backspaceCount = 0;

        for(int k = 0; k < input2.size(); k++){
            if(input2[k] == '#'){
                //update # count
                //don't add to finalize string
                backspaceCount++;
            } 
            else if(backspaceCount > 0 && input2[k] != '#'){
                //letter after backspace is found
                //delete corresponding letters before the #
                
                //final1 should have letter, if not, then its a stray #
                if(final2.empty() || final2.size() < backspaceCount){
                    cout << "False";
                    return;
                }

                //(starting point, length) 
                final2.erase(final2.size() - (backspaceCount), (backspaceCount));
                //reset back count
                backspaceCount = 0;


                //be sure to actually add letter to string
                final2 += input2[k];
            } else {
                // just add to finalized string
                final2 += input2[k];
            }
        }

        // cout << final2;

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

    solution.BackspaceStringCompare("abcde", "abcde");
    cout << ": abcde, abcde";
    cout << "\n";

    solution.BackspaceStringCompare("Uber Career Prep", "u#Uber Careee#r Prep");
    cout << ": Uber Career Prep, u#Uber Careee#r Prep";
    cout << "\n";

    solution.BackspaceStringCompare("abcw#xyz", "abcdef###xyz");
    cout << ": abcdef###xyz, abcw#xyz";
    cout << "\n";

    solution.BackspaceStringCompare("abcdef###xyz", "abcdefxyz###");
    cout << ": abcdef###xyz, abcdefxyz###";
    cout << "\n";

    solution.BackspaceStringCompare("uu##urmo#o#om", "urmom");
    cout << ": uu##urmo#o#om, urmom";
    cout << "\n";

    solution.BackspaceStringCompare("uu###urmo#o#om", "urmom");
    cout << ": uu###urmo#o#om, urmom";
    cout << "\n";
    
    return 0;

}

//time spent on problem: 40+ min
//went overtime sorry :')