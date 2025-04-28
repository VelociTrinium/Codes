#include <iostream>
#include <cstring> 
using namespace std;

class student
{
    public:
        string name;
        int rollNo, total;
        int c;
        void setDetails(string na, int rolNo, int tot)
        {
            name=na;
            rollNo=rolNo;
            total=tot;
        }
        int getFlag()
        {
            return 0;
        }
        void displayDetails()
        {
            if(total<=500)
            {
                int per=(total/5);
                cout<<"Student details:"<<endl;
                cout<<"Name\tRollNo\tTotal\tPercentage"<<endl;
                cout<<name<<"\t"<<rollNo<<"\t"<<total<<"\t"<<(int)per;
            }
            else if(total>500)
            {
                cout<<"Total marks are out of 500";
            }
        }
};

int main() {
    student stu;
    char name[30];
    int rollNo, total;
    cin.getline(name, 30); 
    cin >> rollNo;
    cin >> total;
    stu.setDetails(name, rollNo, total);
    if (stu.getFlag() == 0) {
        stu.displayDetails();
    }
    return 0;
}
