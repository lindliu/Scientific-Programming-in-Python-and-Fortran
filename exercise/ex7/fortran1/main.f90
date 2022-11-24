program myfortran

    ! --- Put use statements here
    !
    ! use mymodule

    implicit none

    ! --- Declare your variables here
    !
    ! integer :: a


    !1.2
    integer :: a, b
    real :: c,d,e
    character :: infile, outfile
    logical :: f
    !1.3
    integer, parameter :: ap=selected_real_kind(14,150)
    real(ap) :: pi

    !2.5
    real, dimension(:), allocatable :: vec
    real, dimension(:,:), allocatable :: mat

    allocate(vec(10))
    allocate(mat(10,20))

    print*, size(mat,2)

    deallocate(vec)
    deallocate(mat)

contains

    ! --- Add your subroutines and functions here
    ! 
    ! subroutine mysub
    ! 
    ! end subroutine mysub

end program myfortran
