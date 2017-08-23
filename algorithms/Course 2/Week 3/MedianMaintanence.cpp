#include <bits/stdc++.h>
using namespace std;

int findmedian(priority_queue<int> &Hlow,priority_queue<int,vector<int>,greater<int> > &Hhigh,int element,int median){

    if(Hlow.size() == Hhigh.size()){
        if(element < median){
            Hlow.push(element);
            median = Hlow.top();
        }
        else{
            Hhigh.push(element);
            median = Hhigh.top();
        }

    }
    else if(Hlow.size() >  Hhigh.size()){
        if(element < median){
            Hhigh.push(Hlow.top());
            Hlow.pop();
            Hlow.push(element);
        }
        else{
            Hhigh.push(element);

        }
		median = Hlow.top();
    }
    else{
        if(element < median){
            Hlow.push(element);

        }
        else{
            Hlow.push(Hhigh.top());
            Hhigh.pop();
            Hhigh.push(element);

        }

        median = Hlow.top();
    }

    return median;
}
int main(){
    priority_queue<int>Hlow;
    long sum = 0;
	priority_queue<int,vector<int>,greater<int> >Hhigh;
    FILE* fp=freopen("Median.txt","r",stdin);
    int number;
    int median = 0;
    int counter = 0;
    while (scanf("%d", &number) > 0) {
        counter++;
        median = findmedian(Hlow,Hhigh,number,median);
        sum = sum  + median;
        cout << "Median " << counter << "---->  " <<median << endl;
    }
    fclose(fp);
    cout <<"Reading .... DOne" << endl;
    cout << "Sum == "<< sum%10000 << endl;
    return 0;
}
