//technique: Forward/backward two-pointer
//time complexity = O(n)
//space complexity = O(n)

#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution{
public:
    string ReverseVowels(string input){
        //have to check for case
        //ASSUMING Y IS NOT A VOWEL !

        bool frontIsVowel = false;
        bool backIsVowel = false;

        //var to keep track of where each vowel is
        int front = 0;
        int back = input.size() - 1;

        while (front < back){

            if(input[front] == 'a' || input[front] == 'A'
            || input[front] == 'e' || input[front] == 'E'
            || input[front] == 'i' || input[front] == 'I'
            || input[front] == 'o' || input[front] == 'O'
            || input[front] == 'u' || input[front] == 'U'
            )
            {
                frontIsVowel = true;
            }

            if(input[back] == 'a' || input[back] == 'A'
            || input[back] == 'e' || input[back] == 'E'
            || input[back] == 'i' || input[back] == 'I'
            || input[back] == 'o' || input[back] == 'O'
            || input[back] == 'u' || input[back] == 'U'
            )
            {
                backIsVowel = true;
            }
                
        
            if(frontIsVowel && backIsVowel){
                //if both are true, switch places
                char holder = input[front];
                input[front] = input[back];
                input[back] = holder;

                //reset bools
                frontIsVowel = false;
                backIsVowel = false;

                //continue w pointers
                front++;
                back--;

            } else if(frontIsVowel){
                //if ONLY front is vowel, move back until vowel is found
                back--;
            } else if(backIsVowel){
                //if ONLY back is vowel, move front until vowel is found
                front++;
            } else {
                //if both false = both not vowels
                //continue w pointers
                front++;
                back--;
            }
        }

            return input;
    }

};

int main(){
    Solution solution;

    cout << "test 1: Uber Career Prep -> " << 
    solution.ReverseVowels("Uber Career Prep") << endl;

    cout << "test 2: xyz -> " << 
    solution.ReverseVowels("xyz") << endl;

    cout << "test 3: flamingo -> " << 
    solution.ReverseVowels("flamingo") << endl;

    cout << "test 4: uuuurmom -> " << 
    solution.ReverseVowels("uuuurmom") << endl;

    cout << "test 5: AEIou -> " << 
    solution.ReverseVowels("AEIou") << endl;

    cout << "test 6: aaeiou -> " << 
    solution.ReverseVowels("aaeiou") << endl;

    return 0;
}

//time spent on problem: 30 min