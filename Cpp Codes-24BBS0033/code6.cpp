#include<iostream>
using namespace std;

class Student
{
    public:
        int rollno, mark1, mark2, mark3;
        void setRno(int n) {rollno=n;}
        void setMark1(int n){mark1=n;}
        void setMark2(int n){mark2=n;}
        void setMark3(int n){mark3=n;}
        int totalMarks() const {return mark1+mark2+mark3;}
        int getrollno() const {return rollno;}
        int getmark1() const {return mark1;}
        int getmark2() const {return mark2;}
        int getmark3() const {return mark3;}
        
        static void findMaxMarks(Student s[], int n)
        {
            int max1=0, r1=0;
            int max2=0, r2=0;
            int max3=0, r3=0;
            for(int i=0; i<n; i++)
            {
                if(s[i].getmark1()>max1)
                {
                    max1=s[i].getmark1();
                    r1=s[i].getrollno();
                }
                if(s[i].getmark2()>max2)
                {
                    max2=s[i].getmark2();
                    r2=s[i].getrollno();
                }
                if(s[i].getmark3()>max3)
                {
                    max3=s[i].getmark3();
                    r3=s[i].getrollno();
                }
            }
            cout<<r1<<" "<<max1<<endl;
            cout<<r2<<" "<<max2<<endl;
            cout<<r3<<" "<<max3<<endl;
        }
        
        static void findMaxTotalMarks(Student s[], int n)
        {
            int max=0, r=0;
            for(int i=0; i<n; i++)
            {
                int total=s[i].totalMarks();
                if(total>max)
                {
                    max=total;
                    r=s[i].getrollno();
                }
            }
            cout<<r<<" "<<max<<endl;
        }
};

int main() {
    int n;
    cin >> n;
    Student s[n];  
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        s[i].setRno(t);
        cin >> t;
        s[i].setMark1(t);
        cin >> t;
        s[i].setMark2(t);
        cin >> t;
        s[i].setMark3(t);
    }
    for (int i = 0; i < n; i++) {
        cout << s[i].totalMarks() << endl;
    }
    Student::findMaxMarks(s, n);
    Student::findMaxTotalMarks(s, n);

    return 0;
}
