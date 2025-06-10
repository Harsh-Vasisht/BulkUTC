# Set minimum CMake version
cmake_minimum_required(VERSION 3.10)

# Project name and language
project(BulkUTC VERSION 1.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set build type if not specified
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

# Set compiler flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g")
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} -O3")

# Add source directories
add_subdirectory(src)

# Set up testing
enable_testing()
add_subdirectory(tests)

# Include configuration files
include_directories(${CMAKE_SOURCE_DIR}/config)

# Set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# Find required packages (example)
# find_package(SomeExternalLibrary REQUIRED)

# Add executable (only if main.cpp exists)
if(EXISTS "${CMAKE_SOURCE_DIR}/src/main.cpp")
    add_executable(${PROJECT_NAME} src/main.cpp)

    # Link libraries
    target_link_libraries(${PROJECT_NAME}
        PRIVATE
        library
        shopping_cart
        university
        # SomeExternalLibrary
    )

    # Install rules
    install(TARGETS ${PROJECT_NAME} DESTINATION bin)
endif()

# Install configuration files
install(DIRECTORY ${CMAKE_SOURCE_DIR}/config DESTINATION etc)

# Add custom target for running tests
add_custom_target(run_tests
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
    DEPENDS ${PROJECT_NAME}
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    COMMENT "Running tests..."
)