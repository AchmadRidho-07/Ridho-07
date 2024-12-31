#include <cctype>
#include <iostream>

int main() {
    char ch = 'a';
    if (std::isalpha(ch)) {
        std::cout << ch << " Adalah huruf." << std::endl;
    }
    std::cout << "Huruf kapitalnya: " << (char)std::toupper(ch) << std::endl; // Output: Uppercase: A
    return 0;
}

