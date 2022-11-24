cmake_minimum_required(VERSION 3.5)

if (APPLE)
        set(CMAKE_Fortran_COMPILER "/usr/local/bin/gfortran")
endif()

project(fortran6 LANGUAGES Fortran)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

file(GLOB fortran_files *.f90)

add_executable(fortran6 my_mod.f90 ${fortran_files})
