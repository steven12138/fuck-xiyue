#include <windows.h>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	int year;
	cout<<"Please Input the Year"<<endl;
	cin>>year;
	cout<<"after you push any key, the program will continue run in 1 sec, so but the mouse into the inputbox"<<endl;
	system("pause");
	Sleep(1000);
	for(int i=1;i<=12;i++)
	{
		
		for(int j=1;j<=31;j++)
		{
			int v=2004;
			stack<int> s2;
			while(v)
			{
				s2.push(v%10);
				v/=10;
			}
			while(!s2.empty())
			{
				int d=s2.top();
				s2.pop();
				keybd_event(char(d+'0'), NULL, KEYEVENTF_EXTENDEDKEY | 0, NULL);
	            keybd_event(char(d+'0'), NULL, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, NULL);
			}
			int e=i;
			stack<int> s1;
			while(e)
			{
				s1.push(e%10);
				e/=10;
			}
			if(i<10)
			s1.push(0);
			while(!s1.empty())
			{
				int d=s1.top();
				s1.pop();
				keybd_event(char(d+'0'), NULL, KEYEVENTF_EXTENDEDKEY | 0, NULL);
	            keybd_event(char(d+'0'), NULL, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, NULL);
			}
			int t=j;
			stack<int> s;
			while(t)
			{
				s.push(t%10);
				t/=10;
			}
			if(j<10)
			s.push(0);
			while(!s.empty())
			{
				int d=s.top();
				s.pop();
				keybd_event(char(d+'0'), NULL, KEYEVENTF_EXTENDEDKEY | 0, NULL);
	            keybd_event(char(d+'0'), NULL, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, NULL);
			}
			keybd_event(VK_RETURN, NULL, KEYEVENTF_EXTENDEDKEY | 0, NULL);
	        keybd_event(VK_RETURN, NULL, KEYEVENTF_EXTENDEDKEY | KEYEVENTF_KEYUP, NULL);
	        Sleep(200);
	        cout<<i<<" "<<j<<endl;
		}
	}
	return 0;
}
