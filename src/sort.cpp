#include "sort.h"
#include <algorithm>
#include <vector>

namespace axelera {

// Template implementation for quicksort
template<typename T>
void quicksort(std::vector<T>& arr, int low, int high) {
    if (low < high) {
        // Partition the array
        T pivot = arr[high];
        int i = low - 1;
        
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                std::swap(arr[i], arr[j]);
            }
        }
        std::swap(arr[i + 1], arr[high]);
        int pi = i + 1;
        
        // Recursively sort elements before and after partition
        quicksort(arr, low, pi - 1);
        quicksort(arr, pi + 1, high);
    }
}

// Specialization for int
void sort(std::vector<int>& arr) {
    if (arr.size() <= 1) return;
    quicksort(arr, 0, arr.size() - 1);
}

// Specialization for float
void sort(std::vector<float>& arr) {
    if (arr.size() <= 1) return;
    quicksort(arr, 0, arr.size() - 1);
}

// Specialization for double
void sort(std::vector<double>& arr) {
    if (arr.size() <= 1) return;
    quicksort(arr, 0, arr.size() - 1);
}

} // namespace axelera

