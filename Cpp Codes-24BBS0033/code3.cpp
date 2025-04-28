#include <iostream>
#include <string>
#include <algorithm> 
using namespace std;

#include <cstring>
class Person
{
    private:
        string name;
        int age;
        string sex;
        
    public:
        void setDetails(const string &name, int age, const string &sex)
        {
            this->name=name;
            this->age=age;
            this->sex=sex;
        }
        string getDetailsInUppercase()
        {
            transform(name.begin(), name.end(), name.begin(), ::toupper);
            transform(sex.begin(), sex.end(), sex.begin(), ::toupper);
            return name + " " + to_string(age) + " " + sex;
        }
};

int main() {
    Person p;
    string name, sex;
    int age;
    cin >> name >> age >> sex;
    p.setDetails(name, age, sex);
    cout << p.getDetailsInUppercase();

    return 0;
}
