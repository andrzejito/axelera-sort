import pytest
import numpy as np
import sys
import os

# Add the build directory to the path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'build'))

try:
    import axelera_sort
except ImportError:
    pytest.skip("axelera_sort module not found. Build the project first.", allow_module_level=True)


class TestSortIntegers:
    def test_empty_list(self):
        arr = []
        result = axelera_sort.sort(arr)
        assert result == []
        assert arr == []

    def test_single_element(self):
        arr = [42]
        result = axelera_sort.sort(arr)
        assert result == [42]
        assert arr == [42]

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        result = axelera_sort.sort(arr)
        assert result == expected
        assert arr == expected

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        result = axelera_sort.sort(arr)
        assert result == expected
        assert arr == expected

    def test_random_array(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        result = axelera_sort.sort(arr)
        assert result == expected
        assert arr == expected

    def test_large_array(self):
        arr = list(range(1000, 0, -1))
        expected = list(range(1, 1001))
        result = axelera_sort.sort(arr)
        assert result == expected
        assert arr == expected

    def test_with_duplicates(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
        result = axelera_sort.sort(arr)
        assert result == expected
        assert arr == expected

    def test_with_negative_numbers(self):
        arr = [-5, -2, -8, 1, 3, -1, 0]
        expected = [-8, -5, -2, -1, 0, 1, 3]
        result = axelera_sort.sort(arr)
        assert result == expected
        assert arr == expected


class TestSortFloats:
    def test_float_array(self):
        arr = [3.14, 1.41, 2.71, 0.57, 1.73]
        expected = [0.57, 1.41, 1.73, 2.71, 3.14]
        result = axelera_sort.sort(arr)
        np.testing.assert_array_almost_equal(result, expected, decimal=10)
        np.testing.assert_array_almost_equal(arr, expected, decimal=10)

    def test_float_with_negative(self):
        arr = [-3.14, 1.41, -2.71, 0.0, 1.73]
        expected = [-3.14, -2.71, 0.0, 1.41, 1.73]
        result = axelera_sort.sort(arr)
        np.testing.assert_array_almost_equal(result, expected, decimal=10)
        np.testing.assert_array_almost_equal(arr, expected, decimal=10)


class TestSortNumpyArrays:
    def test_numpy_int_array(self):
        arr = np.array([64, 34, 25, 12, 22, 11, 90], dtype=np.int32)
        expected = np.array([11, 12, 22, 25, 34, 64, 90], dtype=np.int32)
        result = axelera_sort.sort_array(arr)
        np.testing.assert_array_equal(result, expected)
        np.testing.assert_array_equal(arr, expected)

    def test_numpy_float_array(self):
        arr = np.array([3.14, 1.41, 2.71, 0.57], dtype=np.float32)
        expected = np.array([0.57, 1.41, 2.71, 3.14], dtype=np.float32)
        result = axelera_sort.sort_array(arr)
        np.testing.assert_array_almost_equal(result, expected)
        np.testing.assert_array_almost_equal(arr, expected)

    def test_numpy_double_array(self):
        arr = np.array([3.14, 1.41, 2.71, 0.57], dtype=np.float64)
        expected = np.array([0.57, 1.41, 2.71, 3.14], dtype=np.float64)
        result = axelera_sort.sort_array(arr)
        np.testing.assert_array_almost_equal(result, expected)
        np.testing.assert_array_almost_equal(arr, expected)

    def test_large_numpy_array(self):
        arr = np.random.randint(1, 1000, size=1000, dtype=np.int32)
        expected = np.sort(arr.copy())
        result = axelera_sort.sort_array(arr)
        np.testing.assert_array_equal(result, expected)
        np.testing.assert_array_equal(arr, expected)


class TestPerformance:
    def test_performance_comparison(self):
        import time
        
        # Large array
        size = 100000
        arr1 = list(np.random.randint(1, 1000000, size=size))
        arr2 = arr1.copy()
        
        # Time our C++ implementation
        start = time.time()
        axelera_sort.sort(arr1)
        cpp_time = time.time() - start
        
        # Time Python's built-in sort
        start = time.time()
        arr2.sort()
        python_time = time.time() - start
        
        assert arr1 == arr2
        # C++ should be competitive (at least not orders of magnitude slower)
        # Note: This is a basic check, actual performance may vary
        print(f"\nC++ sort time: {cpp_time:.4f}s")
        print(f"Python sort time: {python_time:.4f}s")

