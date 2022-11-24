module particle_sim

    use mf_datatypes
	use particle_data
	use vector_operations

	implicit none

contains

subroutine update_particle_system(psys, dtin)

    ! Update positions of particle system

	type(particle_system), intent(inout) :: psys
	integer(ik) :: i
    real(dp), intent(in), optional :: dtin
    real(dp) :: dt
	
	if (present(dtin)) then
		dt = dtin
	else
        dt = psys%rmin/(3.0_dp*psys%v0)
	end if 

    ! TODO: Update positions here

end subroutine update_particle_system

subroutine check_boundary(psys)

    ! Check for boundary collision

	type(particle_system), intent(inout) :: psys
	integer(ik) :: i

    ! TODO: Implement boundary collision here

end subroutine check_boundary

subroutine check_collision(psys)

    ! Check for particle particle collission.
    
    type(particle_system), intent(inout) :: psys
        
	integer(ik) :: i, j
    real(dp) :: d, r1, r2
    real(dp) :: vi(3), vj(3)
    real(dp) :: si(3), sj(3)
    real(dp) :: n(3), vdiff(3)
    real(dp) :: q
	
	!       | -------------|
	!               d
	! | --- o --- |   | -- o -- |
	!          r1       r2
	! 
	! collide is true if d < (r1+r2)

    ! TODO: Implement collision algorithm here.
	
end subroutine check_collision

end module particle_sim
