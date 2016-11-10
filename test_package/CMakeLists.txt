project(OpenMeshTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()
conan_set_find_paths()

find_package(OpenMesh REQUIRED)

message("OPENMESH_LIBRARIES: ${OPENMESH_LIBRARIES}")
message("OPENMESH_INCLUDE_DIRS: ${OPENMESH_INCLUDE_DIRS}")
message("OPENMESH_INCLUDE_DIR: ${OPENMESH_INCLUDE_DIR}")

add_executable(test main.cpp)
target_link_libraries(test ${OPENMESH_CORE_LIB} ${OPENMESH_TOOLS_LIB})
target_include_directories(test SYSTEM PRIVATE ${OPENMESH_INCLUDE_DIRS})

set_property(TARGET test PROPERTY CXX_STANDARD 11)
