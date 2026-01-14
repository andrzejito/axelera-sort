#include <catch2/catch_test_macros.hpp>
#include <catch2/catch_template_test_macros.hpp>
#include <vector>
#include <algorithm>
#include <random>
#include "../src/sort.h"

using namespace axelera;

TEMPLATE_TEST_CASE("Sort empty vector", "[sort]", int, float, double) {
    std::vector<TestType> arr;
    sort(arr);
    REQUIRE(arr.empty());
}

TEMPLATE_TEST_CASE("Sort single element", "[sort]", int, float, double) {
    std::vector<TestType> arr = {42};
    sort(arr);
    REQUIRE(arr.size() == 1);
    REQUIRE(arr[0] == 42);
}

TEMPLATE_TEST_CASE("Sort already sorted array", "[sort]", int, float, double) {
    std::vector<TestType> arr = {1, 2, 3, 4, 5};
    std::vector<TestType> expected = arr;
    sort(arr);
    REQUIRE(arr == expected);
}

TEMPLATE_TEST_CASE("Sort reverse sorted array", "[sort]", int, float, double) {
    std::vector<TestType> arr = {5, 4, 3, 2, 1};
    std::vector<TestType> expected = {1, 2, 3, 4, 5};
    sort(arr);
    REQUIRE(arr == expected);
}

TEMPLATE_TEST_CASE("Sort random array", "[sort]", int, float, double) {
    std::vector<TestType> arr = {64, 34, 25, 12, 22, 11, 90};
    std::vector<TestType> expected = {11, 12, 22, 25, 34, 64, 90};
    sort(arr);
    REQUIRE(arr == expected);
}

TEMPLATE_TEST_CASE("Sort large random array", "[sort]", int, float, double) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(1, 1000);
    
    std::vector<TestType> arr(1000);
    for (auto& val : arr) {
        val = static_cast<TestType>(dis(gen));
    }
    
    std::vector<TestType> expected = arr;
    std::sort(expected.begin(), expected.end());
    
    sort(arr);
    REQUIRE(arr == expected);
}

TEMPLATE_TEST_CASE("Sort array with duplicates", "[sort]", int, float, double) {
    std::vector<TestType> arr = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3};
    std::vector<TestType> expected = {1, 1, 2, 3, 3, 4, 5, 5, 6, 9};
    sort(arr);
    REQUIRE(arr == expected);
}

TEMPLATE_TEST_CASE("Sort array with negative numbers", "[sort]", int, float, double) {
    std::vector<TestType> arr = {-5, -2, -8, 1, 3, -1, 0};
    std::vector<TestType> expected = {-8, -5, -2, -1, 0, 1, 3};
    sort(arr);
    REQUIRE(arr == expected);
}

