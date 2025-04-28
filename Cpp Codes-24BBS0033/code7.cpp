#include<iostream>
#include<string>
using namespace std;

class ItemType
{
    private:
        string name;
        double deposit, costPerDay;
    
    public:
        void setName(string na) {name=na;}
        void setDeposit(double depo) {deposit=depo;}
        void setCostPerDay(double cpd) {costPerDay=cpd;}
        string getName() const {return name;}
        double getDeposit() const {return deposit;}
        double getCostPerDay() const {return costPerDay;}
        
};

int main() {
    ItemType obj1;
    string name;
    cin >> name;
    double deposit;
    cin >> deposit;
    double costPerDay;
    cin >> costPerDay;

    obj1.setName(name);
    obj1.setDeposit(deposit);
    obj1.setCostPerDay(costPerDay);
    cout << "Name : " << obj1.getName() << endl;
    cout << "Deposit Amount : " << obj1.getDeposit() << endl;
    cout << "Cost per day : " << obj1.getCostPerDay() << endl;

    return 0;
}
