#include <iostream>
#include <cmath> // Required for the pow() function

class InterestCalculator {
private:
    double principal;
    double rate;
    double time;

public:
    // Constructor to initialize financial data
    InterestCalculator(double p, double r, double t) {
        principal = p;
        rate = r;
        time = t;
    }

    // Method to calculate Simple Interest
    double calculateSimpleInterest() const {
        return (principal * rate * time) / 100.0;
    }

    // Method to calculate Compound Interest (compounded annually)
    double calculateCompoundInterest() const {
        double amount = principal * std::pow((1 + rate / 100.0), time);
        return amount - principal;
    }

    // Method to get the total accumulated amount after compounding
    double getTotalCompoundAmount() const {
        return principal * std::pow((1 + rate / 100.0), time);
    }
};

int main() {
    double p, r, t;

    // User input
    std::cout << "Enter Principal amount: ";
    std::cin >> p;
    std::cout << "Enter Annual Interest Rate (in %): ";
    std::cin >> r;
    std::cout << "Enter Time (in years): ";
    std::cin >> t;

    // Instantiate the Object
    InterestCalculator calculator(p, r, t);

    // Output calculations
    std::cout << "\n--- Results ---" << std::endl;
    std::cout << "Simple Interest: " << calculator.calculateSimpleInterest() << std::endl;
    std::cout << "Compound Interest: " << calculator.calculateCompoundInterest() << std::endl;
    std::cout << "Total Amount (with Compound Interest): " << calculator.getTotalCompoundAmount() << std::endl;

    return 0;
}
