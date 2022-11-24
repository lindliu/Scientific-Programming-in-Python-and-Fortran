program myfortran

    implicit none

    !7.2
    real(4) :: x(21), y(21)
    integer :: i
    !7.3
    integer, parameter :: outfile=10

    x = [( -1 + (i-1) * 0.1, i=1,21 )]

    write(*,'(2A7)') 'x', 'f(x)'
    do i=1,21
        write(*,'(2f7.3)') x(i), sin(x(i))
    end do

!    open(unit=outfile, file='linear.dat', access='sequential', action='write')
!    do i=1,10
!        write(outfile, '(2f7.3)') x(i), sin(x(i))
!    enddo
!    close(outfile)
contains

    ! --- Add your subroutines and functions here
    ! 
    ! subroutine mysub
    ! 
    ! end subroutine mysub

end program myfortran
