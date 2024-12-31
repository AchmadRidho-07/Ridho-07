#include <ctime>
#include <iostream>
int main() {
    time_t now = time(0);
    char* dt = ctime(&now);
    std::cout << "Waktu setempat saat ini: " << dt;
    return 0;
}









