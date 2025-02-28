//1번 카드가 위에, N번 카드가 아래에 
//위에 있는 카드를 바닥에 버리고, 다음으로 위에 있는 카드를 가장 아래로
//위를 1장 남을 때까지 반복
//(위)만 사용 -> queue
//바닥에 버리고 -> pop
//가장 아래로 -> front, push
//1장 남을 때까지-> size
//(출력) front
#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    queue<int> q;

    // 1부터 N까지 큐에 넣기
    for (int i = 1; i <= n; i++) {
        q.push(i);
    }

    // 카드가 1장 남을 때까지 반복
    while (q.size() > 1) {
        q.pop(); // 맨 위 카드 버림
        q.push(q.front()); // 다음 카드를 가장 아래로 이동
        q.pop(); // 이동한 카드 제거
        //pop(): 반환 없음. 단순 삭제
        //front(): 가장 앞(위)에 있는 원소 반환
    }

    // 마지막 남은 카드 출력
    cout << q.front();

    return 0;
}
