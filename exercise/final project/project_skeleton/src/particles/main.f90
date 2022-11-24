program particles

    use mf_datatypes
    use particle_data
    use particle_sim

    implicit none

    type(particle_system) :: psys
    integer(dp) :: i

    ! TODO: Allocate and initialise particle system

    print *, 'Running simulation...'

    call write_particle_sizes(psys)

    ! TODO: Perform particle simulation 
    ! do ...
    !    call check_collision(psys)
    !    ...
    !    call write_particle_positions(psys)
    ! end 

    call print_particle_system(psys)

    print *, 'Deallocating particle system...'

    ! TODO: Deallocate particle system

end program particles
