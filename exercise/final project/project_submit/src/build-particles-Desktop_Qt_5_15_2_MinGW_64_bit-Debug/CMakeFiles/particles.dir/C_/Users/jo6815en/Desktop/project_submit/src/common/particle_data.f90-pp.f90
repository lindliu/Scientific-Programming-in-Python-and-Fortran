# 1 "C:/Users/jo6815en/Desktop/project_submit/src/common/particle_data.f90"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "C:\\Users\\jo6815en\\Desktop\\project_submit\\src\\build-particles-Desktop_Qt_5_15_2_MinGW_64_bit-Debug//"
# 1 "C:/Users/jo6815en/Desktop/project_submit/src/common/particle_data.f90"
 module particle_data

    use mf_datatypes
    use mf_utils

    implicit none

    type particle_system
        integer(ik) :: n_particles
        real(dp) :: x_min, x_max
        real(dp) :: y_min, y_max
        real(dp) :: z_min, z_max
        real(dp) :: v0
        real(dp) :: rmin
        real(dp) :: rmax
        real(dp) :: dt
        real(dp), allocatable :: pos(:,:)
        real(dp), allocatable :: vel(:,:)
        real(dp), allocatable :: r(:)
    end type particle_system

contains

subroutine allocate_particle_system(psys,n)

    ! TODO:
    ! Allocate the pos, vel and r arrays
    ! Initialise the other variables in the particle system
    integer(ik), intent(in) :: n
    type(particle_system) :: psys

    psys % n_particles = n
    psys % x_min = 0_dp
    psys % x_max = 1_dp
    psys % y_min = 0_dp
    psys % y_max = 1_dp
    psys % z_min = 0_dp
    psys % z_max = 1_dp
    psys % v0 = .01_dp
    psys % rmin = .005_dp
    psys % rmax = .015_dp
    psys % dt = psys % rmin/3/psys % v0
    allocate(psys % pos(psys % n_particles, 3))
    allocate(psys % vel(psys % n_particles, 3))
    allocate(psys % r(psys % n_particles))

end subroutine allocate_particle_system

subroutine deallocate_particle_system(psys)

    ! TODO:
    ! Deallocate the pos, vel and r arrays
    ! Set the n_particles variable in psys to -1

    type(particle_system) :: psys

    psys % n_particles = -1
    deallocate(psys % pos)
    deallocate(psys % vel)
    deallocate(psys % r)

end subroutine deallocate_particle_system

subroutine init_particle_system(psys, r_min, r_max, v_min, v_max)

    ! TODO:
    ! Set the initial state of the particle system
    ! 
    ! Random number generator can be initialised with 
    !
    !     call init_random_seed()
    !
    ! Random number can be generated using the following subroutine
    !
    !     call random_number(v)
    !
    ! You can pass an entire array to this functionas well.

    type(particle_system), intent(inout) :: psys
    real(dp) :: r_min, r_max, v_min, v_max

    integer :: i
    real :: v(size(psys%vel,2))

    psys % rmin = r_min
    psys % rmax = r_max

    psys % dt = psys % rmin/3/((v_min+v_max)/2)

    call init_random_seed()

    ! initialize particle radius
    call rand_vec_d(psys % r, psys % rmin, psys % rmax)

    ! initialize particle position
    call rand_mat_d(psys % pos, psys % x_min, psys % x_max)

    ! initialize velocity
    call rand_mat_d(psys % vel, v_min, v_max)
!    psys % vel = psys % v0
    do i = 1, psys%n_particles
        call random_number(v)
        v = sin(v*2*pi)
!        print *, sum((v/sqrt(sum(v**2)))**2)
        psys%vel(i,:) = psys%vel(i,:)*v/sqrt(sum(v**2))
!        print *, sqrt(sum(psys%vel(i,:)**2))
    end do

end subroutine init_particle_system

subroutine print_particle_system(psys)

    type(particle_system), intent(inout) :: psys
    integer(ik) :: i

    print *, 'Max particle x coord = ', maxval(psys%pos(:,1))
    print *, 'Min particle x coord = ', minval(psys%pos(:,1))
    print *, 'Max particle y coord = ', maxval(psys%pos(:,2))
    print *, 'Min particle y coord = ', minval(psys%pos(:,2))
    print *, 'Max particle z coord = ', maxval(psys%pos(:,3))
    print *, 'Min particle z coord = ', minval(psys%pos(:,3))

    !write(*,*) '----- Particle postion - velocity -----------------------------'
    !do i=1,psys%n_particles
    !   write(*,'(2F12.5,A5,2F12.5)') psys%pos(i,:), '-', psys%vel(i,:)
    !end do

	!write(*,*) '----- Particle size -------------------------------------------'
	!do i=1,psys%n_particles
	!        write(*,'(F12.5)') psys%r(i)
	!end do

end subroutine print_particle_system

subroutine write_particle_sizes(psys)

    type(particle_system), intent(inout) :: psys
    integer(ik) :: i

        open(unit=15, file='particle.state', access='APPEND')
	write(15, '(I10)') psys%n_particles
	do i = 1,psys%n_particles
		write(15, '(F12.5)') psys%r(i)
	end do
	close(unit=15)	

end subroutine write_particle_sizes

subroutine write_particle_positions(psys)

    type(particle_system), intent(inout) :: psys
    integer(ik) :: i

        open(unit=15, file='particle.state', access='APPEND')
	write(15, '(I10)') psys%n_particles
	do i = 1,psys%n_particles
		write(15, '(3F12.5)') psys%pos(i,:)
	end do
        close(unit=15)
	
end subroutine write_particle_positions

end module particle_data
