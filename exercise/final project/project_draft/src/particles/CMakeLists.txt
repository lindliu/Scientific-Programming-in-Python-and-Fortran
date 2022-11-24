
cmake_minimum_required(VERSION 3.5)

project(particles LANGUAGES Fortran)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

add_executable(particles ../common/mf_datatypes.f90 ../common/mf_utils.f90
../common/particle_data.f90 ../common/particle_sim.f90 ../common/particle_state.f90 ../common/vector_operations.f90 main.f90)
