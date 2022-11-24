program myfortran

    ! --- Put use statements here
    !
    ! use mymodule
    use my_mod

    implicit none

    ! --- Declare your variables here
    !
    ! integer :: a

    !6.1
    real :: x=1
    real :: out

    !6.2
    real, dimension(10) :: data_
    real :: mean, var
    integer :: n

    call fun6_1(x,out)
    print *, out


    data_ = (/2.,1.5,1.,1.,3.,1.,2.,1.,.5,1./)
    n = size(data_)
    call fun6_2(data_,n,mean,var)
    print *, mean, var, n
contains

    ! --- Add your subroutines and functions here
    ! 
    ! subroutine mysub
    ! 
    ! end subroutine mysub

end program myfortran
