program myfortran

    ! --- Put use statements here
    !
    ! use mymodule

    implicit none

    ! --- Declare your variables here
    !
    ! integer :: a

    !8.1
    character(len=7) :: c1='Fortran'
    character(len=2) :: c2='is'
    character(len=3) :: c3='fun'
    character(:), allocatable :: c4


    !8.2
    character(len = 32) :: s
    integer, parameter :: ap=selected_real_kind(15,30)
    real(ap) :: f

    c4 = c1//' '//c2//' '//c3
    print *, c4


    s = '.1'
    call convert(s, f)
    print *, f

contains

    ! --- Add your subroutines and functions here
    ! 
    ! subroutine mysub
    ! 
    ! end subroutine mysub
    subroutine convert(s, f)
        character(len = 32) :: s
        integer, parameter :: ap=selected_real_kind(15,30)
        real(ap) :: f

        read(s, *) f
    end subroutine

end program myfortran
