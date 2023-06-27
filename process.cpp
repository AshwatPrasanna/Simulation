#include <iostream>
#include <cmath>

int calculate_changes(int n) {
    int changes = (n ^ (n >> 1));
    
    int count = 0;
    while (changes != 0) {
        count++;
        changes = changes & (changes - 1);
    }
    return count - 1;
}

int calculate_hnum(int n) {
    int hnum = 0;
    for (int i = (1 << (n - 1)); i < (1 << n); i++) {
        int changes = calculate_changes(i);

        if (changes > hnum) {
            int changes_3n = calculate_changes(i * 3);

            if (changes_3n - changes > 0) {
                hnum = changes;
            }
        }
    }
    return hnum;
}

int main(int argc, char* argv[]) {
    std::cout << calculate_hnum(std::stoi(argv[1])) << std::endl;
    return 0;
}
