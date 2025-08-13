#include <immintrin.h>
#include <stdio.h>

int main() {
    unsigned int rand;
    if (_rdrand32_step(&rand)) {
        printf("Hardware random: %u\n", rand);
    } else {
        printf("Failed to generate random number\n");
    }
    return 0;
}
