module particle_driver

    use mf_datatypes
	use particle_data
	use particle_sim
	use particle_state

	implicit none

contains

subroutine init_system(n, r_min, r_max, v_min, v_max)

	integer(ik), intent(in) :: n
        real(8), intent(in) :: r_max, r_min
        real(8), intent(in) :: v_max, v_min
	
	print *, 'Allocating particle system...'
	call allocate_particle_system(psys, n)
	print *, 'Initialising particle system...'
	call init_particle_system(psys, r_min, r_max, v_min, v_max) 

end subroutine init_system

subroutine get_positions(coords)
	real(8), intent(inout) :: coords(:,:)
	integer(ik) :: i
	coords = psys%pos
end subroutine get_positions	

subroutine get_sizes(sizes)
	real(8), intent(inout) :: sizes(:)
	sizes = psys%r
end subroutine get_sizes

subroutine write_sizes()
	call write_particle_sizes(psys)
end subroutine write_sizes

subroutine collision_check()
	call check_collision(psys)
end subroutine collision_check

subroutine boundary_check()
	call check_boundary(psys)
end subroutine boundary_check

subroutine update()
	call update_particle_system(psys)
end subroutine update

subroutine write_positions()
	call write_particle_positions(psys)
end subroutine write_positions

subroutine deallocate_system()
	call deallocate_particle_system(psys)
end subroutine deallocate_system

end module particle_driver
