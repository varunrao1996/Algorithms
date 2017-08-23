#include <bits/stdc++.h>
using namespace std;
#include <string>
#include <sstream>
#define INF 999999
#include<limits.h>
int totalcost = 0;

int findmin(map<int,int> &distance,map<int,int> &visited){
    int mini = INT_MAX;
    int index = -1;
    for(map<int,int>::iterator it = distance.begin();it != distance.end();it++){
        if (it->second < mini && visited[it->first] == 0){
                index = it->first;
                mini = it->second;
        }
    }
    return index;

}
void prim(map<int,vector< pair <int,int> > > graph, map<int,int> &visited, map<int,int> &distance){

    for(int i = 1;i <=graph.size();i++){
        int get_min = findmin(distance,visited);
        totalcost += distance[get_min];
        visited[get_min] = 1;
        for(int j = 0; j < graph[get_min].size();j++){
            if(visited[graph[get_min][j].first] == 0 && graph[get_min][j].second < distance[graph[get_min][j].first])
                distance[graph[get_min][j].first] = graph[get_min][j].second ;
        }
    }
}
int main(){
    map<int,vector< pair <int,int> > > graph;
    map<int,int> visited;
    map<int,int> distance;
    FILE *fp = freopen("edges.txt","r",stdin);
	int nodes = 0;
    int edges = 0;
    scanf("%d %d", &nodes,&edges);
	int source;
    int destination;
    int cost;
    while (scanf("%d %d %d", &source, &destination,&cost) > 0) {
           graph[source].push_back(make_pair(destination,cost));
           graph[destination].push_back(make_pair(source,cost));
           visited[source] = 0;
           visited[destination] = 0;
           distance[source] = INF;
           distance[destination] = INF;
    }
    fclose(fp);
    distance[1] = 0;
    prim(graph,visited,distance);

    cout << totalcost << endl;
    return 0;
}

