#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;


    vector<int> has_cpp(n + 1, 0);
    vector<int> has_java(n + 1, 0);


    for (int i = 0; i < m; i++) {
        int p, L;
        cin >> p >> L;
        if (L == 1) {
            has_cpp[p] = 1;
        } else if (L == 2) {
            has_java[p] = 1;
        }
    }

    for (int i = 1; i <= n; i++) {
        if (has_cpp[i] && has_java[i]) {
            cout << i << endl;
        }
    }

    return 0;
}
