#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string add_base(string num1, string num2, vector<char> symbols);
int index_in(char c, vector<char> symbols);

int main() {
	int base;
	cin >> base;
	vector<char> symbols;
	string symbol_string;
	cin >> symbol_string;
	for (int i=0; i<base; i++) {
		symbols.push_back(symbol_string[i]);
	}
	string num1, num2, line, questionmarks;
        cin >> num1;
        cin.ignore(256, '\n');
        cin.get(); //get rid of that pesky '+'
        cin >> num2 >> line >> questionmarks;	
	
	string result = add_base(num1, num2, symbols);
	
	int width = line.length();

	printf("%d %s\n", base, symbol_string.c_str());
	printf("%*s\n", width, num1.c_str());
	printf("+%*s\n", width-1, num2.c_str());
	printf("%s\n", line.c_str());
	printf("%*s", width, result.c_str());

	return 0;
}

string add_base(string num1, string num2, vector<char> symbols) {
	bool num1_longer = num1.length() >= num2.length(); 
	int base = symbols.size();

	if (!num1_longer) {
		string temp = num1;
		num1 = num2;	
		num2 = temp;
	}

	//pad num2 with leading 0 symbols
	int pad = num1.length() - num2.length();
	for (int i=0; i<pad; i++) {
		num2 = symbols[0] + num2;
	}
	
	bool carry = false;
	string result = "";
	for (int i=num2.length()-1; i>=0; i--) {
		int added = carry + index_in(num2[i], symbols) + index_in(num1[i], symbols);
		if (added >= base) {
			carry = true;
			added -= base;
		} else {
			carry = false;
		}
		result = symbols[added] + result;
	}
	if (carry)
		result = symbols[1] + result;
	
	return result;
}

int index_in(char c, vector<char> symbols) {
	for (int i=0; i<symbols.size(); i++) {
		if (c == symbols[i])
			return i;
	}
	return -1;
}
