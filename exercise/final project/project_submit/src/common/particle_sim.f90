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
        dt = psys%dt
    end if

    ! TODO: Update positions here

    do i=1,psys%n_particles
        psys%pos(i,:) = psys%pos(i,:)+psys%vel(i,:)*dt
    end do

end subroutine update_particle_system

subroutine check_boundary(psys)

    ! Check for boundary collision

	type(particle_system), intent(inout) :: psys
	integer(ik) :: i

    ! TODO: Implement boundary collision here
    do i = 1, psys%n_particles
        if (psys%pos(i,1)-psys%r(i)<=psys%x_min) then
            psys%vel(i,1) = abs(psys%vel(i,1))
        else if (psys%pos(i,1)+psys%r(i)>=psys%x_max) then
            psys%vel(i,1) = -abs(psys%vel(i,1))
        end if

        if (psys%pos(i,2)-psys%r(i)<=psys%y_min) then
            psys%vel(i,2) = abs(psys%vel(i,2))
        else if (psys%pos(i,2)+psys%r(i)>=psys%y_max) then
            psys%vel(i,2) = -abs(psys%vel(i,2))
        end if

        if (psys%pos(i,3)-psys%r(i)<=psys%z_min) then
            psys%vel(i,3) = abs(psys%vel(i,3))
        else if (psys%pos(i,3)+psys%r(i)>=psys%z_max) then
            psys%vel(i,3) = -abs(psys%vel(i,3))
        end if

    end do
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

    do i = 1, psys%n_particles
        do j = i+1, psys%n_particles
            vi = psys%vel(i,:)
            vj = psys%vel(j,:)
            si = psys%pos(i,:)
            sj = psys%pos(j,:)

            d = sqrt(sum((si-sj)**2))
            r1 = psys%r(i)
            r2 = psys%r(j)
!            print *, d, r1, r2

            if (d<(r1+r2)) then
                psys%vel(i,:) = vi+dot_product(vj-vi, sj-si)/d**2 * (sj-si)
                psys%vel(j,:) = vj+dot_product(vi-vj, sj-si)/d**2 * (sj-si)
            end if
        end do
    end do
end subroutine check_collision

end module particle_sim
