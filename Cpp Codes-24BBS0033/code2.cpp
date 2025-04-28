#include <iostream>
using namespace std;

class VoC
{
    public:
        char c;
        VoC(char inputChar)
        {
            c = inputChar;
        }
        string checkAlpha()
        {
            if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u')
            {
                return "Vowel";
            }
            else
            {
                return "Consonant";
            }
        }
};

int main() {
    char c;
    cin >> c;  
    VoC voc(c); 
    cout << c << " : " << voc.checkAlpha();
    return 0;
}
