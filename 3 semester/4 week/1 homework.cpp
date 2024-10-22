#include <iostream>
#include <cmath>
using namespace std;

struct vectors {
    unsigned n;
    
    float* create () {
        float* teg = new float[n];
        float x;
        for (int i = 0; i < n; i++)
        {
            std::cin >> x;
            teg[i] = x;
        }
        return teg;
    }

    void reading (float* teg) {
        std::cout << "Vector = {";
        for (int i = 0; i < (n-1); i++) 
        {
            std::cout << teg[i] << ", ";
        }
        std::cout << teg[n-1] << "}" << std::endl;
    }

    float* scalar_calc (float* teg, float a) {
        float* scalar_teg = new float[n];
        for (int i = 0; i < n; i++)
        {
            scalar_teg[i] = teg[i] * a;
        }
        return scalar_teg;
    }

    float* vector_calc (float* teg1, float* teg2) {
        float* vector_teg = new float[n];
        for (int i = 0; i < n; i++)
        {
            vector_teg[i] = teg1[i] + teg2[i];
        }
        return vector_teg;
    }

    float scalar_comp (float* teg1, float* teg2) {
        float ans = 0;
        for (int i = 0; i < n; i++)
        {
            ans = ans + teg1[i]*teg2[i];
        }
        return ans;
    }

};

int main() {
    float N;
    std::cin >> N;
    struct vectors Dim;
    Dim.n = N;
    float* vector1 = Dim.create();
    Dim.reading(vector1);
    float* scalar_vector = Dim.scalar_calc(vector1, 3);
    Dim.reading(scalar_vector);
    float* vector_vector = Dim.vector_calc(vector1, scalar_vector);
    Dim.reading(vector_vector);
    Dim.reading(scalar_vector);
    Dim.reading(vector1);
    float answer = Dim.scalar_comp(vector1, scalar_vector);
    std::cout << answer;

    delete[] vector1;
    delete[] scalar_vector;
    delete[] vector_vector;

    return 0;
}