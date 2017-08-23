#include <bits/stdc++.h>
using namespace std;
#define INF 99999999
double length = 0.0;

void readdata(int nodes,vector<pair<double,double>> &cities,vector<int> &vis){
    int n;
    for(int i=0;i<nodes;i++){
        double a,b;
        scanf("%d %lf %lf",&n,&a,&b);
        cities.push_back(make_pair(a,b));
        vis[i]=0;
    }
}
double euclidean(int current,int other,vector<pair<double,double>> &cities){
    double x = pow(cities[current].first - cities[other].first,2);
    double y = pow(cities[current].second - cities[other].second,2);
    double z = x+y;
    return z;
}
int findnextnode(int nodes,int current,vector<pair<double,double>> &cities,vector<int> &vis)
{
    double nearest=INF;
    int next = -1;
    for(int j=0;j<nodes;j++)
    {
        double dis = euclidean(current,j,cities);
        if(dis< nearest && vis[j]==0)
        {
            nearest = dis;
            next = j;
        }
    }

    length = length + sqrt(nearest);
    cout << "Node " << next <<" is selected with length = " << (long)nearest << endl;
    return next;
}
double TSP(int nodes,vector<pair<double,double>> &cities,vector<int> &vis){
    int current = 0;
    vis[current] = 1;

    cout << "Node 0 is seleted with length = " << (long)length << endl;
    for(int i=1;i<nodes;i++)
    {
        vis[current] = 1;
        current = findnextnode(nodes,current,cities,vis);
        
    }
    double xx = pow(cities[current].first - cities[0].first,2);
    double yy = pow(cities[current].second - cities[0].second,2);
    length += sqrt(xx + yy);
    cout << "Node 0"<<" is selected with length = " << (long)(sqrt(xx+yy)) << endl;
    return length;
}
int main()
{
    FILE *fp = freopen("nn.txt","r",stdin);
    int nodes;
    scanf("%d",&nodes);
    vector<pair<double,double>> cities;
    vector<int> vis(nodes,0);
    readdata(nodes,cities,vis);
    cout<<"Shortest Cycle(Approx.) = " << (long)TSP(nodes,cities,vis) << endl;
}
