# Quick Start Guide - Step by Step

This guide walks you through building and testing the Axelera AI sorting library.

## Option 1: Using Docker (Easiest)

### Step 1: Build the Docker Image
```bash
docker build -t axelera-sort .
```

### Step 2: Run Tests (Automatic)
```bash
docker run --rm axelera-sort
```

The container will automatically:
- Build the project
- Run C++ tests
- Run Python tests

### Step 3: Interactive Development (Optional)
```bash
docker run -it --rm axelera-sort bash
```

Inside the container:
- Project is in `/workspace`
- Built files are in `/workspace/build`
- You can modify code and rebuild

---

## Option 2: Manual Build on Linux

### Step 1: Install System Dependencies
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
```

### Step 2: Install Python Dependencies
```bash
pip3 install -r requirements.txt
```

This installs:
- pybind11 (for Python bindings)
- pytest (for Python testing)
- numpy (for NumPy support)

### Step 3: Install Catch2 (for C++ Testing)

**Option A: Using Git (Recommended)**
```bash
git clone --branch v3.5.2 --depth 1 https://github.com/catchorg/Catch2.git /tmp/Catch2
cd /tmp/Catch2
cmake -B build -S . -DBUILD_TESTING=OFF
cmake --build build
sudo cmake --install build
```

**Option B: Let CMake Fetch It**
CMake will automatically download Catch2 if not found (configured in CMakeLists.txt).

### Step 4: Build the Project
```bash
# Create build directory
mkdir -p build
cd build

# Configure CMake
cmake .. -DBUILD_TESTING=ON -DBUILD_PYTHON_BINDINGS=ON

# Build (use -j4 for 4 parallel jobs, or -j$(nproc) for all cores)
cmake --build . -j$(nproc)
```

### Step 5: Run Tests

**C++ Tests:**
```bash
cd build
ctest --output-on-failure
```

**Python Tests:**
```bash
cd build
python3 -m pytest ../tests/test_python.py -v
```

**Or run both using Make:**
```bash
make test
```

### Step 6: Try the Example
```bash
cd build
PYTHONPATH=. python3 ../example_usage.py
```

---

## Option 3: Using Makefile (Linux/macOS)

The project includes a Makefile for convenience:

```bash
# Check dependencies
make check

# Build everything
make build

# Run all tests
make test

# Clean build artifacts
make clean

# Build and test in one command
make all
```

---

## Option 4: Using setup.py (Alternative Python Build)

This is an alternative to CMake for Python-only builds:

```bash
# Install dependencies
pip3 install -r requirements.txt

# Build and install
pip3 install -e .

# Run tests
python3 -m pytest tests/test_python.py -v
```

---

## Verification Checklist

After building, verify everything works:

- [ ] C++ library compiles without errors
- [ ] Python module can be imported: `python3 -c "import axelera_sort"`
- [ ] C++ tests pass: `cd build && ctest`
- [ ] Python tests pass: `cd build && python3 -m pytest ../tests/test_python.py -v`
- [ ] Example script runs: `PYTHONPATH=build python3 example_usage.py`

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'axelera_sort'"

**Solution:**
```bash
# Make sure you're in the build directory or set PYTHONPATH
export PYTHONPATH=$PWD/build:$PYTHONPATH
python3 -c "import axelera_sort"
```

### "CMake Error: Could not find pybind11"

**Solution:**
```bash
pip3 install pybind11
# Or let CMake fetch it automatically (already configured)
```

### "CMake Error: Could not find Catch2"

**Solution:**
CMake will automatically download Catch2 if not found. If you want to install manually:
```bash
# See Step 3 in Option 2 above
```

### Build fails with "undefined reference"

**Solution:**
Make sure you're building from a clean state:
```bash
rm -rf build
mkdir build
cd build
cmake ..
cmake --build .
```

---

## Project Structure Overview

```
.
├── src/                    # C++ source code
│   ├── sort.h             # Header file
│   └── sort.cpp           # Implementation
├── python_bindings/        # Python bindings
│   └── pybindings.cpp     # pybind11 bindings
├── tests/                  # Test files
│   ├── test_sort.cpp      # C++ tests (Catch2)
│   └── test_python.py     # Python tests (pytest)
├── CMakeLists.txt         # CMake build configuration
├── Dockerfile             # Docker container definition
├── Makefile               # Convenience Makefile
├── requirements.txt       # Python dependencies
├── setup.py              # Alternative Python build
├── README.md             # Full documentation
└── QUICKSTART.md         # This file
```

---

## Next Steps

1. **Review the code**: Check `src/sort.cpp` and `python_bindings/pybindings.cpp`
2. **Run tests**: Ensure all tests pass
3. **Try examples**: Run `example_usage.py` to see the library in action
4. **Read README.md**: For detailed documentation and API reference

---

## Key Files to Review for Assessment

The assessors will likely focus on:

1. **CMakeLists.txt** - Build system configuration
2. **Dockerfile** - Containerized development environment
3. **tests/** - Comprehensive test coverage
4. **README.md** - Documentation quality
5. **Build reproducibility** - Can they build it easily?

Make sure all of these are polished and working!

