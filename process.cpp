#include <iostream>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>

using namespace std;

int changes(long long unsigned int num) {
    long long unsigned int changesbit = (((num << 1)^(num))>>1);

    // Kernighan's algorithm to count number of set bits
    int count = 0;

    while (changesbit>0) {
        changesbit = changesbit&(changesbit-1);
        count++;
    }

    return count-1;
}

int calculate_h_k(long long unsigned int lower, long long unsigned int upper) {
    int h_k = 0;

    for (long long unsigned int i = lower; i<upper; i++) {
        int c = changes(i);

        if (c > h_k) {
            if (changes(3*i) >= c) {
                h_k = c;
            }
        }
    }

    return h_k;
}

int main(int argc, char* argv[]) {

    if (argc != 3) {
        throw ("Needs 2 arguments exactly!"); // These are the bounds, inclusive, exclusive respectively
    }
    
    long long unsigned int lowerlimit = (long long unsigned int)stoll(string(argv[1]));
    long long unsigned int upperlimit = (long long unsigned int)stoll(string(argv[2]));

    cout << "Using range " << lowerlimit << ":" << upperlimit;

    return calculate_h_k(lowerlimit, upperlimit);
}

