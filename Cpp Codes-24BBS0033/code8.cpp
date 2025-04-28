#include<iostream>
using namespace std;

class BMI
{
    private:
        int n;
        float m;
        char c;
    
    public:
        char bmi(int n, float m)
        {
            float bmi=n/(m*m);
            if(bmi<18.5) c='U';
            else if (bmi>=18.5 and bmi<25.0) c='N';
            else if (bmi>=25.0 and bmi<30.0) c='H';
            else if (bmi>=30.0) c='O';
            return c;
        }
        
    
};

int main() {
    int n;           
    cin >> n;       
    float m;         
    cin >> m;   
    BMI t;          
    char grade = t.bmi(n, m);
    cout << grade << endl;

    return 0;
}
