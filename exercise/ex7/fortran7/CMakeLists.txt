cmake_minimum_required(VERSION 3.5)

if (APPLE)
        set(CMAKE_Fortran_COMPILER "/usr/local/bin/gfortran")
endif()

project(fortran7 LANGUAGES Fortran)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

file(GLOB fortran_files *.f90)

add_executable(fortran7 ${fortran_files})
