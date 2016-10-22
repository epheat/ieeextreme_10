#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<vector<int> > get_empty_maze();
bool open_room(int row, int col, vector<vector<int> > &open_rooms, vector<vector<int> > &connected_rooms);


int main() {
	
	vector<vector<int> > open_rooms, connected_rooms;
	open_rooms = get_empty_maze();
	connected_rooms = get_empty_maze();
	
	int row, col;
	int rooms_opened = 0;
	bool connected_path_exists = false;

	//continually get new rooms to open, until there are no more to get or until a connected path exists
	while (!connected_path_exists && cin >> row >> col) {
		
		connected_path_exists = open_room(row, col, open_rooms, connected_rooms);
		rooms_opened++;
	}
	
	if (connected_path_exists)	
		cout << rooms_opened;
	else
		cout << -1;

	return 0;
}

vector<vector<int> > get_empty_maze() {
	
	int N;
	cin >> N;
	vector<vector<int> > maze;

	for (int i=0; i<N; i++) {
		vector<int> row;
		for (int j=0; j<N; j++) {
			row.push_back(0);
		}
		maze.push_back(row);
	}
	return maze;
}

bool open_room(int row, int col, vector<vector<int> > &open_rooms, vector<vector<int> > &connected_rooms) {
	
	open_rooms[row][col] = 1;
	
	
	
	
	
	
	
	
	return false;	
}

