#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
    int n;
    cin >> n;

    vector<ll> v(n);  
    for(int i = 0; i < n; i++) {
        cin >> v[i];
    }

    ll speed = v[n - 1];

    for(int i = n - 2; i >= 0; i--) {
        ll vi = v[i];
        if (speed % vi != 0) {
            speed = (speed / vi + 1) * vi;
        }
    }

    cout << speed << '\n';
}

