program particles

    use mf_datatypes
    use particle_data
    use particle_sim

    implicit none

    type(particle_system) :: psys
    integer(dp) :: i
    integer(ik) :: n
    real(dp) :: rmin, rmax, v_min, v_max

    ! TODO: Allocate and initialise particle system
    rmin = 0.005
    rmax = 0.01
    v_min = 0.01
    v_max = 0.09

    n = 200
    call allocate_particle_system(psys,n)
    call init_particle_system(psys, rmin, rmax, v_min, v_max)

    print *, 'Running simulation...'


    call write_particle_sizes(psys)
    call write_particle_positions(psys)
    ! TODO: Perform particle simulation
    ! do ...
    !    call check_collision(psys)
    !    ...
    !    call write_particle_positions(psys)
    ! end

    do i=1,1000
        call check_boundary(psys)
        call check_collision(psys)

        call update_particle_system(psys)

        call write_particle_positions(psys)
    end do

    call print_particle_system(psys)

    print *, 'Deallocating particle system...'

    ! TODO: Deallocate particle system
    call deallocate_particle_system(psys)




end program particles
