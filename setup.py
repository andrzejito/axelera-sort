from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, Extension
import pybind11
import numpy

ext_modules = [
    Pybind11Extension(
        "axelera_sort",
        [
            "python_bindings/pybindings.cpp",
            "src/sort.cpp",
        ],
        include_dirs=[
            "src",
            numpy.get_include(),
        ],
        language='c++',
        cxx_std=17,
    ),
]

setup(
    name="axelera_sort",
    version="1.0.0",
    author="Axelera AI",
    description="Efficient sorting library with C++ backend",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
    ],
)

