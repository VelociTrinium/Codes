#include <iostream>
using namespace std;

class Student
{
    private:
        int score[5];
        
    public:
        void input()
        {
            for(int i=0;i<5;i++)
            {
                cin>>score[i];
            }
        }
        int calculateTotalScore()
        {
            int TotalScore=0;
            for(int i=0; i<5; i++)
            {
                TotalScore+=score[i];
            }
            return TotalScore;
        }
        static int countHigherScores(Student *s, int n)
        {
            int kscore = s[0].calculateTotalScore();
            int c=0;
            for(int i=1; i<n; i++)
            {
                if(s[i].calculateTotalScore()>kscore)
                    c++;
            }
            return c;
        }
};

int main() {
    int n;
    cin >> n;

    // Dynamically allocate an array of Student objects
    Student *s = new Student[n];

    // Input scores for all students
    for (int i = 0; i < n; i++) {
        s[i].input();
    }

    // Call the static method to count how many students scored higher than Kristen
    int result = Student::countHigherScores(s, n);

    // Output the result
    cout << result << endl;

    // Free dynamically allocated memory
    delete[] s;

    return 0;
}
