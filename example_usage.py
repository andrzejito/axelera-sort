#!/usr/bin/env python3
"""
Example usage of the Axelera AI sorting library.

Make sure to build the project first:
    cd build && cmake .. && cmake --build .

Then run this script:
    PYTHONPATH=build python3 example_usage.py
"""

import sys
import os

# Add build directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'build'))

try:
    import axelera_sort
    import numpy as np
except ImportError as e:
    print(f"Error: Could not import axelera_sort. Make sure the project is built.")
    print(f"Build instructions: cd build && cmake .. && cmake --build .")
    sys.exit(1)


def main():
    print("=" * 60)
    print("Axelera AI Sorting Library - Example Usage")
    print("=" * 60)
    
    # Example 1: Sort a list of integers
    print("\n1. Sorting a list of integers:")
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"   Before: {numbers}")
    axelera_sort.sort(numbers)
    print(f"   After:  {numbers}")
    
    # Example 2: Sort floats
    print("\n2. Sorting a list of floats:")
    floats = [3.14, 1.41, 2.71, 0.57, 1.73]
    print(f"   Before: {floats}")
    axelera_sort.sort(floats)
    print(f"   After:  {floats}")
    
    # Example 3: Sort with negative numbers
    print("\n3. Sorting with negative numbers:")
    mixed = [-5, -2, -8, 1, 3, -1, 0]
    print(f"   Before: {mixed}")
    axelera_sort.sort(mixed)
    print(f"   After:  {mixed}")
    
    # Example 4: Sort NumPy array
    print("\n4. Sorting a NumPy array:")
    arr = np.array([64, 34, 25, 12, 22, 11, 90], dtype=np.int32)
    print(f"   Before: {arr}")
    axelera_sort.sort_array(arr)
    print(f"   After:  {arr}")
    
    # Example 5: Performance comparison
    print("\n5. Performance comparison (large array):")
    import time
    
    size = 100000
    test_data = np.random.randint(1, 1000000, size=size)
    
    # C++ implementation
    arr1 = test_data.copy()
    start = time.time()
    axelera_sort.sort_array(arr1)
    cpp_time = time.time() - start
    
    # NumPy sort
    arr2 = test_data.copy()
    start = time.time()
    arr2.sort()
    numpy_time = time.time() - start
    
    print(f"   Array size: {size:,} elements")
    print(f"   C++ sort time:  {cpp_time:.4f} seconds")
    print(f"   NumPy sort time: {numpy_time:.4f} seconds")
    print(f"   Speedup: {numpy_time/cpp_time:.2f}x")
    
    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

