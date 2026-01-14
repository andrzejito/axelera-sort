#ifndef SORT_H
#define SORT_H

#include <vector>

namespace axelera {

/**
 * Efficient sorting function that sorts a vector of integers in-place
 * Uses quicksort algorithm for optimal performance
 * 
 * @param arr Reference to vector that will be sorted in-place
 */
void sort(std::vector<int>& arr);

/**
 * Efficient sorting function that sorts a vector of floats in-place
 * 
 * @param arr Reference to vector that will be sorted in-place
 */
void sort(std::vector<float>& arr);

/**
 * Efficient sorting function that sorts a vector of doubles in-place
 * 
 * @param arr Reference to vector that will be sorted in-place
 */
void sort(std::vector<double>& arr);

} // namespace axelera

#endif // SORT_H

