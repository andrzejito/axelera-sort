cmake_minimum_required(VERSION 3.15)
project(AxeleraSort VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Build options
option(BUILD_TESTING "Build tests" ON)
option(BUILD_PYTHON_BINDINGS "Build Python bindings" ON)

# Find Python3
if(BUILD_PYTHON_BINDINGS)
    find_package(Python3 COMPONENTS Interpreter Development NumPy REQUIRED)
    
    # Find pybind11 - try to find it first, then use FetchContent if not found
    find_package(pybind11 QUIET)
    if(NOT pybind11_FOUND)
        include(FetchContent)
        FetchContent_Declare(
            pybind11
            GIT_REPOSITORY https://github.com/pybind/pybind11.git
            GIT_TAG        v2.11.1
        )
        FetchContent_MakeAvailable(pybind11)
    endif()
endif()

# Include directories
include_directories(src)

# Library source files
set(LIB_SOURCES
    src/sort.cpp
    src/sort.h
)

# Create the static library
add_library(axelera_sort_lib STATIC ${LIB_SOURCES})

# Set include directories for the library
target_include_directories(axelera_sort_lib PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src>
    $<INSTALL_INTERFACE:include>
)

# Build Python bindings
if(BUILD_PYTHON_BINDINGS)
    pybind11_add_module(axelera_sort python_bindings/pybindings.cpp)
    target_link_libraries(axelera_sort PRIVATE axelera_sort_lib pybind11::module pybind11::lto pybind11::windows_extras)
    target_include_directories(axelera_sort PRIVATE ${Python3_NumPy_INCLUDE_DIRS})
    
    # Set output directory for Python module
    set_target_properties(axelera_sort PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}
    )
endif()

# Build tests
if(BUILD_TESTING)
    enable_testing()
    
    # Find or fetch Catch2
    find_package(Catch2 3 QUIET)
    if(NOT Catch2_FOUND)
        include(FetchContent)
        FetchContent_Declare(
            Catch2
            GIT_REPOSITORY https://github.com/catchorg/Catch2.git
            GIT_TAG        v3.5.2
        )
        FetchContent_MakeAvailable(Catch2)
    endif()
    
    list(APPEND CMAKE_MODULE_PATH ${Catch2_SOURCE_DIR}/extras)
    include(Catch)
    
    # C++ tests
    add_executable(test_sort tests/test_sort.cpp)
    target_link_libraries(test_sort PRIVATE axelera_sort_lib Catch2::Catch2WithMain)
    catch_discover_tests(test_sort)
    
    # Python tests (run via pytest)
    add_test(NAME PythonTests COMMAND ${Python3_EXECUTABLE} -m pytest ${CMAKE_CURRENT_SOURCE_DIR}/tests/test_python.py -v)
    set_tests_properties(PythonTests PROPERTIES
        ENVIRONMENT "PYTHONPATH=${CMAKE_BINARY_DIR}:$ENV{PYTHONPATH}"
    )
endif()

# Installation
install(TARGETS axelera_sort_lib
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)

install(FILES src/sort.h
    DESTINATION include/axelera
)

if(BUILD_PYTHON_BINDINGS)
    install(TARGETS axelera_sort
        LIBRARY DESTINATION ${Python3_SITEARCH}
    )
endif()

