#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

#define DEBUG_MODE false

using namespace std;

vector<vector<int> > get_empty_maze(int N);
bool open_room(int row, int col, vector<vector<int> > &open_rooms, vector<vector<int> > &connected_rooms);
int adjacent_to_open_room(int row, int col, vector<vector<int> > &rooms);
bool update_adjacent_rooms(int row, int col, vector<vector<int> > &open_rooms, vector<vector<int> > &connected_rooms);
void print_state(vector<vector<int> > &open_rooms, vector<vector<int> > &connected_rooms);

int main() {
	
	vector<vector<int> > open_rooms, connected_rooms;
	int N;
	cin >> N;
	open_rooms = get_empty_maze(N);
	connected_rooms = get_empty_maze(N);
	
	int row, col;
	int rooms_opened = 0;
	bool connected_path_exists = false;

	//continually get new rooms to open, until there are no more to get or until a connected path exists
	while (!connected_path_exists && (cin >> row >> col)) {
		
		//send row-1 and col-1 to the function, because room numbering starts at (1,1)
		connected_path_exists = open_room(row-1, col-1, open_rooms, connected_rooms);
		rooms_opened++;
		if (DEBUG_MODE)
			print_state(open_rooms, connected_rooms);
	}
	
	if (connected_path_exists)	
		cout << rooms_opened;
	else
		cout << -1;

	return 0;
}

vector<vector<int> > get_empty_maze(int N) {
	
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
	int N = open_rooms.size();
	bool con_room_added = false;
	
	if (DEBUG_MODE)
		cout << "opening room: row" << row << " col" << col << "\n"; 

	open_rooms[row][col] = 1;
	
	if (row == 0) {
		connected_rooms[row][col] = 1;
		con_room_added = true;
	}

	if (adjacent_to_open_room(row, col, connected_rooms)) {
		connected_rooms[row][col] = 1;
		con_room_added = true;
	}
	
	if (con_room_added) {
		if (row == N-1) {
			return true;
		} else {
			// check if, by adding the room, any more rooms should be added to the connected_rooms list
			if (update_adjacent_rooms(row, col, open_rooms, connected_rooms))
				return true;

		}
	}
	
	return false;	
}

//returns 1 if the room north of row, col is open
//returns 2 if the room east of row, col is open
//returns 3 if the room south of row, col is open
//returns 4 if the room west of row, col is open
//returns 0 if no adjacent room is open
int adjacent_to_open_room(int row, int col, vector<vector<int> > &rooms) {
	int N = rooms.size();
	
	//check in the order north, east, south, west
	
	if (row-1 >= 0 && rooms[row-1][col] == 1)
		return 1;
	if (col+1 < N && rooms[row][col+1] == 1)
		return 2;
	if (row+1 < N && rooms[row+1][col] == 1)
		return 3;
	if (col-1 >= 0 && rooms[row][col-1] == 1)
		return 4;

	return 0;
}

bool update_adjacent_rooms(int row, int col, vector<vector<int> > &open_rooms, vector<vector<int> > &connected_rooms) {
	int N = connected_rooms.size();
	
	// if we're updating the adjacent rooms on a room in the last row, we've concluded that there is a path from top to bottom
	if (row == N-1)
		return true;

	// update in the order north, east, south, west
	
	if (row-1 >= 0 && connected_rooms[row-1][col] == 0 && open_rooms[row-1][col] == 1) {
		connected_rooms[row-1][col] = 1;
		if (update_adjacent_rooms(row-1, col, open_rooms, connected_rooms))
			return true;
	}
	if (col+1 <  N && connected_rooms[row][col+1] == 0 && open_rooms[row][col+1] == 1) {
		connected_rooms[row][col+1] = 1;
		if (update_adjacent_rooms(row, col+1, open_rooms, connected_rooms))
			return true;
	}
	if (row+1 <  N && connected_rooms[row+1][col] == 0 && open_rooms[row+1][col] == 1) {
		connected_rooms[row+1][col] = 1;
		if (update_adjacent_rooms(row+1, col, open_rooms, connected_rooms))
			return true;
	}
	if (col-1 >= 0 && connected_rooms[row][col-1] == 0 && open_rooms[row][col-1] == 1) {
		connected_rooms[row][col-1] = 1;
		if (update_adjacent_rooms(row, col-1, open_rooms, connected_rooms))
			return true;
	}

	return false;
}

void print_state(vector<vector<int> > &open_rooms, vector<vector<int> > &connected_rooms) {
	int N = open_rooms.size();
	cout << "open_rooms\tconnected_rooms\n";
	
	for (int i=0; i<N; i++) {
		cout << "[";
		for (int j=0; j<N; j++) {
			cout << open_rooms[i][j];
		}
		cout << "]\t\t[";
		for (int j=0; j<N; j++) {
			cout << connected_rooms[i][j];
		}
		cout << "]\n";
	}


}



