#include <iostream>
#include <climits>
using namespace std;

int find_min_index(int dist[], bool isSet[], int n){
	int min = INT_MAX;
	int res;
	for(int i=0; i<n; ++i){
		if(!isSet[i] && dist[i] <= min){
			min = dist[i];
			res = i;
		}
	}
	return res;
}

void print_distance_table(int dist[], int n){
	cout << "Vertex   Distance from source" << endl;
	for(int i=0; i<n; ++i){
		cout << i << "\t\t" << dist[i] << endl;
	}
}

void dijkstras(int n, int **g, int src){
	int * dist = new int[n];
	bool * isSet = new bool[n];
	for(int i=0; i<n; ++i){
		dist[i] = INT_MAX;
		isSet[i] = false;
	}
	dist[src] = 0;
	for(int cnt = 0; cnt < n-1; ++cnt){
		int u = find_min_index(dist, isSet, n);
		// cout << "u is: " << u << endl;
		// cout << "dist[u] " << dist[u] << endl;
		isSet[u] = true;
		// update dist[]
		for(int i=0; i<n; ++i){
			// VERY IMPORTANT!!!
			int tmp = ((int *)g+u*n)[i];
			// cout << "tmp: " << tmp << endl;
			if( dist[u] < INT_MAX && !isSet[i] && tmp && dist[i] > dist[u] + tmp){
				dist[i] = dist[u] + tmp;
			}
		}
	}
	print_distance_table(dist, n);
	delete[] dist;
	delete[] isSet;
}

int main(){
	int graph[][9] = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                      {4, 0, 8, 0, 0, 0, 0, 11, 0},
                      {0, 8, 0, 7, 0, 4, 0, 0, 2},
                      {0, 0, 7, 0, 9, 14, 0, 0, 0},
                      {0, 0, 0, 9, 0, 10, 0, 0, 0},
                      {0, 0, 4, 0, 10, 0, 2, 0, 0},
                      {0, 0, 0, 14, 0, 2, 0, 1, 6},
                      {8, 11, 0, 0, 0, 0, 1, 0, 7},
                      {0, 0, 2, 0, 0, 0, 6, 7, 0}};

    dijkstras(9, (int **)graph, 0);
    // dijkstras(9, graph, 0);

	return 0;
}