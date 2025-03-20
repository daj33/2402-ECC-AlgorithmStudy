//힌트: 필요한 입력만 받는다
//최대 힙 사용할 경우
//힙 크기가 n보다 작을 때
//n번째로 큰 원소보다 큰 원소가 등장했을 때 -> 기존 n번째 원소 제거 필요 -> 최대힙?!
//최소 힙으로 구현하기

#include <iostream>
#include <queue>

using namespace std;

struct cmp {
    bool operator()(const int &parent, const int &child) {
        return parent > child;
    }
};
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    
	int n; 
	cin >> n;
    
	priority_queue<int, vector<int>, cmp> pq;
    int x;
    for(int i=0; i<n*n; i++){
        cin >> x;
        if(pq.size()>=n){
            if(pq.top() <= x) {
                pq.pop();
                pq.push(x);
            }
        }
        else pq.push(x);
    }
    
    cout << pq.top();
    return 0;
}

