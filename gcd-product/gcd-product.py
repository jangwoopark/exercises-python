#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define min(x , y) (x)<(y)?(x):(y)

const long long mod = 1000000007;
const int lu = 20000000 ;
int ciur[lu] ;

void umple(long long n){
    for(long long i = 2 ; i <= n ; i ++){
        if(ciur[i] == 0){
            for(long long j = i ; j * i <= n ; j ++){
                ciur[i * j] = 1 ;
            }
        }
    }
}

long long putere(long long x , long long y){
    long long put = 1 ;
    while(y){
        if(y & 1){
            put = (put * x) % mod ;
        }
        x = (x * x) % mod ;
        y /= 2 ;
    }
    return put ;
}
int main() {
    long long n , m ;
    cin >> n >> m ;
    if(m == 1 || n == 1){
        cout << 1 ;
    }
    long long mini = min(n , m) ;
    umple(mini) ;
    long long rez = 1 ;
    for(long long i = 2 ; i <= mini ; i ++){
        if(ciur[i] == 0){
            long long x = i ;
            while(mini >= x){
                long long exp = (n / x) * (m / x) ;
                exp = exp % (mod - 1) ;
                rez = (rez * putere(i , exp)) % mod ;
                x = x * i ;
            }
        }
    }
    cout << rez ;
    return 0;
}
