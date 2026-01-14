#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "../src/sort.h"

namespace py = pybind11;
using namespace axelera;

PYBIND11_MODULE(axelera_sort, m) {
    m.doc() = "Axelera AI efficient sorting library with C++ backend";
    
    // Helper function to sort Python lists in-place
    m.def("sort", [](py::list arr) {
        if (arr.empty()) return arr;
        
        // Check the type of the first element to determine the type
        py::object first = arr[0];
        bool is_int = py::isinstance<py::int_>(first);
        bool is_float = py::isinstance<py::float_>(first);
        
        if (is_int) {
            // Integer list
            std::vector<int> vec;
            for (auto item : arr) {
                vec.push_back(py::cast<int>(item));
            }
            sort(vec);
            for (size_t i = 0; i < vec.size(); ++i) {
                arr[i] = vec[i];
            }
        } else if (is_float) {
            // Float list - use double for Python floats (64-bit)
            std::vector<double> vec;
            for (auto item : arr) {
                vec.push_back(py::cast<double>(item));
            }
            sort(vec);
            for (size_t i = 0; i < vec.size(); ++i) {
                arr[i] = vec[i];
            }
        } else {
            // Try to cast as int, then float, then double
            try {
                std::vector<int> vec;
                for (auto item : arr) {
                    vec.push_back(py::cast<int>(item));
                }
                sort(vec);
                for (size_t i = 0; i < vec.size(); ++i) {
                    arr[i] = vec[i];
                }
            } catch (...) {
                try {
                    std::vector<double> vec;
                    for (auto item : arr) {
                        vec.push_back(py::cast<double>(item));
                    }
                    sort(vec);
                    for (size_t i = 0; i < vec.size(); ++i) {
                        arr[i] = vec[i];
                    }
                } catch (...) {
                    throw std::runtime_error("Unsupported type in list");
                }
            }
        }
        return arr;
    }, "Sort a list of numbers in-place (supports int, float, double)",
    py::arg("arr"));
    
    m.def("sort_array", [](py::array_t<int> arr) {
        auto buf = arr.request();
        int* ptr = static_cast<int*>(buf.ptr);
        std::vector<int> vec(ptr, ptr + buf.size);
        sort(vec);
        std::copy(vec.begin(), vec.end(), ptr);
        return arr;
    }, "Sort a numpy array of integers in-place",
    py::arg("arr"));
    
    m.def("sort_array", [](py::array_t<float> arr) {
        auto buf = arr.request();
        float* ptr = static_cast<float*>(buf.ptr);
        std::vector<float> vec(ptr, ptr + buf.size);
        sort(vec);
        std::copy(vec.begin(), vec.end(), ptr);
        return arr;
    }, "Sort a numpy array of floats in-place",
    py::arg("arr"));
    
    m.def("sort_array", [](py::array_t<double> arr) {
        auto buf = arr.request();
        double* ptr = static_cast<double*>(buf.ptr);
        std::vector<double> vec(ptr, ptr + buf.size);
        sort(vec);
        std::copy(vec.begin(), vec.end(), ptr);
        return arr;
    }, "Sort a numpy array of doubles in-place",
    py::arg("arr"));
}

