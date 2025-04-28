#include <iostream>
using namespace std;
class AddAmount
{
    public:
    int amount=50;
    AddAmount()
    {
        amount = 50;
    }
    AddAmount(int a)
    {
        amount+=a;
    }
    void print_amount()
    {
        cout<<amount;
    }
};

int main()
{
    AddAmount a1;
int amt;
    cin>>amt;
    AddAmount a2(amt);
    a2.print_amount();
    return 0;
} 