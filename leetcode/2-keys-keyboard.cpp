#include <vector>
#include <unordered_map>
#include <assert.h>

using namespace std;

class Solution {
public:
    int minSteps(int n) {
        vector<int> primes = getPrimes(n);
        vector<int> factors = getFactors(n, primes);
        unordered_map<int, int> steps;
        int value = 1;
        steps[1] = 0;

        for (int f: factors) {
            steps[value * f] = steps[value] + f;
            value = value * f;
            // cout << "factor: " << f << ", value: " << value << endl;
        }

        return steps[n];
    }

    vector<int> getPrimes(const int n) {
        vector<bool> sieve(n+1);
        vector<int> primes;

        sieve[2] = true;
        int i = 2;
        while (i <= n) {
            primes.push_back(i);
            for (int j=i; j<=n; j+=i) {
                sieve[j] = true;
            }

            int next = i+1;
            while (next <= n/2) {
                if (!sieve[next]) break;
                next++;
            }
            i = next;
        }

        return primes;
    }

    vector<int> getFactors(int n, vector<int>& primes) {
        vector<int> factors;
        int i = 0;
        while (n != 1 && i < primes.size()) {
            if (n % primes[i] == 0) {
                factors.push_back(primes[i]);
                n = n / primes[i];
            } else {
                i++;
            }
        }
        return factors;
    }
};

int main() {
    Solution s;
    assert(s.minSteps(2) == 2);
    assert(s.minSteps(3) == 3);
    assert(s.minSteps(37) == 37);
    assert(s.minSteps(50) == 12);
    assert(s.minSteps(100) == 14);
    assert(s.minSteps(250) == 17);
    assert(s.minSteps(500) == 19);
    assert(s.minSteps(750) == 20);
    assert(s.minSteps(999) == 46);
}
