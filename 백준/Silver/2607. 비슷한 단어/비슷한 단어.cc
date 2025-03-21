#include<iostream>
#include<string>
#include<vector>

using namespace std;

vector<int> getComposition(string s)
{   
    vector<int> cmp (26, 0);
    int len = s.length();
    for(int i=0; i<len; i++)
    {
        int alph = s[i] - 'A';
        cmp[alph]++;
    }
    
    return cmp;
}
 vector<int> getDifference(vector<int> cmp_first, vector<int> cmp_other)
{
    vector<int> diff (26, 0);
    
    for(int i=0; i<26; i++){
        if(cmp_first[i] != cmp_other[i]) diff[i] = cmp_first[i] - cmp_other[i];
    }
    return diff;
}
bool isSimilar(vector<int> diff){
    int plus = 0;
    int minus = 0;
    for(int i=0; i<26; i++){
        if(abs(diff[i])>1) return false;
        if(diff[i] == 0) continue;
        if(diff[i] == 1) plus++;
        else if(diff[i] == -1) minus--;
    }
    return (plus == 0 && minus == 0) || (plus == 1 && minus == 0) || (plus == 0 && minus == -1) || (plus == 1 && minus == -1);
}
int main()
{
    //입력
    int n;
    cin >> n;
    string first, other;
    cin >> first;
    
    //연산
    int answer = 0;
    vector<int> cmp_f = getComposition(first);
    while(--n){
        cin >> other;
        vector<int> cmp_o = getComposition(other);
        vector<int> diff = getDifference(cmp_f, cmp_o);
        if(isSimilar(diff)) answer++;
    }
    //출력
    cout << answer;
    return 0;
}