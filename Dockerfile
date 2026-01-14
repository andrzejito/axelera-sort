FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    python3 \
    python3-dev \
    python3-pip \
    python3-numpy \
    libpython3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install --no-cache-dir \
    pybind11 \
    pytest \
    numpy

# Install Catch2 for testing
RUN git clone --branch v3.5.2 --depth 1 https://github.com/catchorg/Catch2.git /tmp/Catch2 && \
    cd /tmp/Catch2 && \
    cmake -B build -S . -DBUILD_TESTING=OFF && \
    cmake --build build && \
    cmake --install build && \
    rm -rf /tmp/Catch2

# Set working directory
WORKDIR /workspace

# Copy project files
COPY . .

# Build the project
RUN mkdir -p build && \
    cd build && \
    cmake .. -DBUILD_TESTING=ON -DBUILD_PYTHON_BINDINGS=ON && \
    cmake --build . -j$(nproc)

# Run tests
RUN cd build && \
    ctest --output-on-failure && \
    python3 -m pytest ../tests/test_python.py -v

# Default command
CMD ["/bin/bash"]

