#include <iostream>
#include <iomanip>
using namespace std;

class student
{
    private:
        char na[31];
        int rolNo, tot;
        float pre;
    
    public:
        int flag=1;
        void initDetails()
        {
            cin>>na;
            cin>>rolNo;
            cin>>tot;
            pre=tot/5.0;
            
            int length=0;
            while(na[length]!='\0') {length++;}            
            if(length<=30 and (rolNo>=1 and rolNo<=10000) and (tot>=0 and tot<=500))
                cout << na << " " << rolNo << " " << tot << " " << fixed << setprecision(1) << pre;
            else
                cout<<"Invalid";
        }
        void getDetails(char* &name, int &rollNo, int &total, float &perc)
        {
            name=na;
            rollNo=rolNo;
            total=tot;
            perc=pre;
        }
};

int main() {
    student stu;
    stu.initDetails();

    if (stu.flag == 0) {
        char* name;
        int rollNo, total;
        float perc;

        stu.getDetails(name, rollNo, total, perc);

        cout << name << " " << rollNo << " " << total << " " << fixed << setprecision(1) << perc;
    }

    return 0;
}
