// Dog Walking - problem 1
// Evan Heaton, Ryan Shah, & Jacob Pawlak

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

int find_optimal_distribution(int dogs, int walkers, vector<int> dog_sizes);
string vec_to_string(vector<int> v);

int main() {
	
	int test_cases;
	cin >> test_cases;

	//for each test case, load all the data.
	for (int i=0; i<test_cases; i++) {
		int dogs, walkers;
		cin >> dogs >> walkers;
		
		vector<int> dog_sizes;
		//for each dog, get its size and put it in the dog_sizes vector
		for (int j=0; j<dogs; j++) {
			int size;
			cin >> size;
			dog_sizes.push_back(size);
		}
		
		cout << vec_to_string(dog_sizes) << "\n";
		int sum_of_ranges = find_optimal_distribution(dogs, walkers, dog_sizes);
		cout << sum_of_ranges << "\n";
	}

	return 0;
}

int find_optimal_distribution(int dogs, int walkers, vector<int> dog_sizes) {
	
	return 1;
}

string vec_to_string(vector<int> v) {
	if (v.size() == 0) {
		return "<>";
	}
	stringstream ss;
	ss << "<";
	for (int i=0; i<v.size()-1; i++) {
		ss << v[i] << ", ";
	}
	ss << v[v.size()-1] << ">";
	return ss.str();
}
