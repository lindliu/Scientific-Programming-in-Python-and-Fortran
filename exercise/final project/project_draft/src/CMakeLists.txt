
cmake_minimum_required(VERSION 3.5)

project(particles)
enable_language(Fortran CXX C)
set(CMAKE_INCLUDE_CURRENT_DIR ON)


subdirs(particle-lib particles)
