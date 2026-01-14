
# Axelera AI Sorting Library

An efficient Python library for sorting arrays, with the compute-intensive sorting logic implemented in C++ for optimal performance.

## Overview

This library provides high-performance sorting capabilities by delegating the computationally intensive sorting operations to a C++ backend, while exposing a clean Python API that's easy to use for engineers who don't need to worry about C++ implementation details.

## Features

- **High Performance**: C++ implementation using optimized quicksort algorithm
- **Multiple Data Types**: Supports integers, floats, and doubles
- **Python Bindings**: Clean Python API using pybind11
- **NumPy Support**: Direct support for NumPy arrays
- **Comprehensive Testing**: Unit tests for both C++ and Python sides
- **Docker Support**: Containerized development environment

## Requirements

### System Requirements
- **OS**: Linux, macOS, or Windows (with appropriate build tools)
- **C++ Compiler**: GCC 7+ or Clang 8+ (C++17 support required)
- **CMake**: Version 3.15 or higher
- **Python**: 3.7 or higher
- **pip**: For installing Python dependencies

### Dependencies
- **pybind11**: For Python bindings
- **Catch2**: For C++ unit testing (v3.x)
- **pytest**: For Python unit testing
- **numpy**: For NumPy array support

## Quick Start

### Using Docker (Recommended)

The easiest way to build and test the library is using Docker:

```bash
# Build the Docker image
docker build -t axelera-sort .

# Run the container (tests will run automatically)
docker run --rm axelera-sort

# Or run interactively
docker run -it --rm axelera-sort bash
```

Inside the container, the project is already built in `/workspace/build`.

### Manual Build

#### 1. Install Dependencies

**On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y \
    build-essential \
    cmake \
    python3 \
    python3-dev \
    python3-pip \
    python3-numpy \
    libpython3-dev

pip3 install -r requirements.txt
```

**On macOS (using Homebrew):**
```bash
brew install cmake python3
pip3 install -r requirements.txt
```

**On Windows:**
- Install Visual Studio 2019 or later with C++ development tools
- Install CMake from https://cmake.org/download/
- Install Python 3.7+ from python.org
- Run: `pip install -r requirements.txt`

#### 2. Install Catch2 (for C++ tests)

```bash
git clone --branch v3.5.2 --depth 1 https://github.com/catchorg/Catch2.git /tmp/Catch2
cd /tmp/Catch2
cmake -B build -S . -DBUILD_TESTING=OFF
cmake --build build
sudo cmake --install build
```

Alternatively, CMake will try to find Catch2 if it's installed system-wide.

#### 3. Build the Project

```bash
# Create build directory
mkdir -p build
cd build

# Configure CMake
cmake .. -DBUILD_TESTING=ON -DBUILD_PYTHON_BINDINGS=ON

# Build
cmake --build . -j$(nproc)  # Use -j4 or similar on macOS/Windows
```

#### 4. Run Tests

**C++ Tests:**
```bash
cd build
ctest --output-on-failure
# Or run directly:
./test_sort
```

**Python Tests:**
```bash
cd build
python3 -m pytest ../tests/test_python.py -v
```

Or from the project root:
```bash
PYTHONPATH=build python3 -m pytest tests/test_python.py -v
```

## Usage

### Python API

#### Basic Usage

```python
import axelera_sort

# Sort a list of integers
numbers = [64, 34, 25, 12, 22, 11, 90]
axelera_sort.sort(numbers)
print(numbers)  # [11, 12, 22, 25, 34, 64, 90]

# Sort floats
floats = [3.14, 1.41, 2.71, 0.57]
axelera_sort.sort(floats)
print(floats)  # [0.57, 1.41, 2.71, 3.14]
```

#### NumPy Array Support

```python
import numpy as np
import axelera_sort

# Sort a NumPy array
arr = np.array([64, 34, 25, 12, 22, 11, 90], dtype=np.int32)
axelera_sort.sort_array(arr)
print(arr)  # [11, 12, 22, 25, 34, 64, 90]
```

### C++ API

```cpp
#include "sort.h"
#include <vector>

using namespace axelera;

int main() {
    std::vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    sort(arr);
    // arr is now sorted: {11, 12, 22, 25, 34, 64, 90}
    return 0;
}
```

## Project Structure

```
.
├── CMakeLists.txt          # Main CMake build configuration
├── Dockerfile              # Docker container definition
├── requirements.txt        # Python dependencies
├── setup.py               # Python package setup (alternative build)
├── README.md              # This file
├── src/
│   ├── sort.h            # C++ header file
│   └── sort.cpp          # C++ implementation
├── python_bindings/
│   └── pybindings.cpp    # Python bindings using pybind11
└── tests/
    ├── test_sort.cpp     # C++ unit tests (Catch2)
    └── test_python.py    # Python unit tests (pytest)
```

## Build System Details

### CMake Configuration

The build system uses CMake with the following options:

- `BUILD_TESTING`: Enable/disable test building (default: ON)
- `BUILD_PYTHON_BINDINGS`: Enable/disable Python bindings (default: ON)

Example:
```bash
cmake .. -DBUILD_TESTING=ON -DBUILD_PYTHON_BINDINGS=ON
```

### Alternative: Using setup.py

You can also build and install the Python module using setuptools:

```bash
pip install .
# Or for development:
pip install -e .
```

## Testing

### Running All Tests

```bash
cd build
ctest --output-on-failure          # C++ tests
python3 -m pytest ../tests/test_python.py -v  # Python tests
```

### Test Coverage

The test suite includes:

**C++ Tests:**
- Empty vector handling
- Single element arrays
- Already sorted arrays
- Reverse sorted arrays
- Random arrays
- Large arrays (1000+ elements)
- Arrays with duplicates
- Arrays with negative numbers

**Python Tests:**
- All C++ test cases ported to Python
- NumPy array support
- Performance comparison tests
- In-place sorting verification

## Performance

The C++ implementation uses an optimized quicksort algorithm, providing:
- O(n log n) average case time complexity
- O(n²) worst case (rare with random data)
- In-place sorting (O(1) space complexity)

For large arrays (100,000+ elements), the C++ implementation typically shows significant performance improvements over Python's built-in sort.

## Troubleshooting

### Import Error: Module not found

If you get `ModuleNotFoundError: No module named 'axelera_sort'`:

1. Ensure the project is built: `cd build && cmake --build .`
2. Add build directory to PYTHONPATH: `export PYTHONPATH=$PWD/build:$PYTHONPATH`
3. Or run tests from build directory: `cd build && python3 -m pytest ../tests/test_python.py`

### CMake can't find pybind11

Install pybind11:
```bash
pip3 install pybind11
# Or install system-wide:
# sudo apt-get install pybind11-dev  # Ubuntu/Debian
```

### CMake can't find Catch2

Install Catch2 as described in the Requirements section, or let CMake download it:
```bash
cmake .. -DCatch2_DIR=/path/to/Catch2
```

## Development

### Adding New Features

1. Add C++ implementation in `src/sort.cpp`
2. Update header in `src/sort.h`
3. Add Python bindings in `python_bindings/pybindings.cpp`
4. Add tests in `tests/`
5. Rebuild: `cd build && cmake --build .`

### Code Style

- C++: Follow Google C++ Style Guide
- Python: Follow PEP 8
- Use meaningful variable names
- Add comments for complex logic

## License

This project is created for the Axelera AI build engineer assessment.

## Contact

For questions about this implementation, please refer to the assessment instructions.

