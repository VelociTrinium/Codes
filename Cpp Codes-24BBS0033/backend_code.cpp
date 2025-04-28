#include <iostream>
#include <iomanip>
#include <cstring>
using namespace std;

int Size_people = 15; 
string Rank_People[15][2] = {{"24BBS0001", "1"},{"24BBS0002", "2"},{"24BBS0003", "3"},{"24BBS0004", "4"},{"24BBS0005", "5"},
							{"24BBS0006", "6"},{"24BBS0007", "7"},{"24BBS0008", "8"},{"24BBS0009", "9"},{"24BBS0010", "10"},
							{"24BBS0011", "11"},{"24BBS0012", "12"},{"24BBS0013", "13"},{"24BBS0014", "14"},{"24BBS0015", "15"}};



int main()
{
	//collect data
	string ID, Rank;
	for(int i=15; i>0; i--)
	{
		ID = Rank_People[Size_people-i][0];
		Rank = Rank_People[Size_people-i][1];
//		cout<<ID<<"\t"<<Rank<<endl;
	}
	
	//process data
	
	
	
	
	return 0;
}
