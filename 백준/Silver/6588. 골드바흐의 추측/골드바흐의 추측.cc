#include <iostream>
#include <vector>

using namespace std;

const int LIMIT = 1000000;

vector<bool> is_prime(LIMIT + 1, true);
vector<int> primes; // 소수 리스트

void findPrime() {
    is_prime[0] = is_prime[1] = false; 
    // 0과 1은 소수가 아님
    for (int i = 2; i * i <= LIMIT; i++) {
        // 제곱근
        if (is_prime[i]) {
            for (int j = i * i; j <= LIMIT; j += i) {
                // i * 2 >> 중복 제거
                is_prime[j] = false; 
                // i의 배수 제거
            }
        }
    }

    // 소수 리스트 저장
    for (int i = 2; i <= LIMIT; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
        }
    }
}


int main() {
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    findPrime(); // 소수를 미리 계산

    while (true) {
        int n;
        cin >> n;
        if (n == 0) return 0; // 종료

        bool valid = false; // 골드바흐 검증
        
        // 합으로 나타내기
       for (int prime : primes) {
            if (prime >= n) break; 
           // n보다 큰 소수는 필요 없음
            if (is_prime[n - prime]) { 
                // n - prime도 소수인지 확인
                printf("%d = %d + %d\n", n, prime, n - prime);
                valid = true;
                break;
            }
        }

        if (!valid) {
            printf("Goldbach's conjecture is wrong.\n");
        }
    }
    return 0;
}
