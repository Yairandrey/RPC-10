#include <iostream>
#include <cmath>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int round_number, position;
    cin >> round_number >> position;

    if (position == 1) {
        cout << round_number << endl;
        return 0;
    }

    position = pow(2, round_number) - position + 1;

    while (pow(2, round_number) > position) {
        round_number--;
    }

    cout << round_number + 1 << endl;

    return 0;
}
