// s -> a1, ..., an
// x+d, x-d 이동
// 가능한 d의 최댓값 구하기 
// d의 최댓값: s와 동생 위치의 차들의 최대공약수

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath> 

using namespace std;
int euclidean(int a, int b){
    if(b == 0) return a;
    return euclidean(b, a%b);
}
int main(){
    //입력
    int n, s;
    cin >> n >> s;
    vector<int> loc(n, 1);
    
     for(int i=0; i < n; i++){
        int k;
        cin >> k;
        loc[i] = abs(s - k);
    }
  
    //처리 
    int gcd = loc[0];
    for(int i = 0; i < n ; i++){
        gcd = euclidean(gcd, loc[i]);
    }
    
    //출력
    cout << gcd;
    
    return(0);  
}
