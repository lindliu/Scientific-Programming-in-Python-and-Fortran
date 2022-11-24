program myfortran

    ! --- Put use statements here
    !
    ! use mymodule

    implicit none

    ! --- Declare your variables here
    !
    ! integer :: a

    !2.7
    integer :: num(100)
    integer :: i, init_=3, end_=10

    !integer :: A(100)
    !integer :: i

    !integer :: i1
    !integer :: i2

    !A = (/ (i, i=1,size(A,1)) /)

    !i1 = 10
    !i2 = 20

    !A(i1:i2) = A(i2:i1:-1)

    !write(*, '(100I5)') (A(i), i=1,100)

    !2.9
    real, dimension(50,20) :: a


    num = (/(i, i=1,100)/)
    print *, "initial data: ", num(init_), "end data: ", num(end_)
    print *, "reverse: ", num(end_:init_:-1)

    a = 0
    a(1,:) = 1
    print *, a
    a(:, ubound(a,2)) = 2
    print *, a
    a(1:ubound(a,1):2, 1:ubound(a,2):2) = 3
    print *, a
    a(ubound(a,1):1:-2, ubound(a,2):1:-2) = 3
    print *, a

contains

    ! --- Add your subroutines and functions here
    ! 
    ! subroutine mysub
    ! 
    ! end subroutine mysub

end program myfortran
