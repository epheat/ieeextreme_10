#include <iostream>
#include <vector>

using namespace std;

long gcd(long a, long b) {
        while(a != b) {
            if(a > b) {
                a = a - b;
            } else {
                b = b - a;
            }
        }
        return a;
}

long inti(long n, long a, long b) {
        long low = 0;
        long count = 0;
        double mid = 0;
        for(int i = a; i <= b; i++) {
                if(gcd(n, i) == 1) {
                    low = i;
                    break;
                }
        }
        //cout << count << endl;
    long high = 0;
    for(int i = b; i >= a; i--) {
        if(gcd(i, n) == 1) {
            high = i;
            break;
        }
    }
    mid = (high + low) / 2.0;
    for(int i = a; i < mid; i++) {
        if(gcd(i, n) == 1) {
            count++;
        }
    }
    long sum = (low+high) * count;
    return (sum % 1000000007);
}

int main() {

        int stu;
        cin >> stu;
        while(stu > 0) {
                long n, a, b;
                cin >> n;
                cin >> a;
                cin >> b;
                cout << inti(n, a, b) << endl;
                stu--;
        }

}
