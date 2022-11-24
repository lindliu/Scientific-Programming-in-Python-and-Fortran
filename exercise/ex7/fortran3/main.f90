program myfortran

    ! --- Put use statements here
    !
    ! use mymodule

    implicit none

    ! --- Declare your variables here
    !
    ! integer :: a

    !3.1
    integer :: i=300
    logical :: extra_filling=.true.

    !3.2
    integer :: a=1

    !4.1
    integer :: j

    !5.1
    real :: x=3, y=4
    !5.2
    real :: E(5,3), F(3,5), G(5,5), H(10)


    if (i>100) then
        print *, i, " is greater than 100!"
    end if

    if (extra_filling) then
        print *, "Extra filling is ordered"
    else
        print *, "No extra filling"
    end if


    select case(a)
        case(1)
            write(*,*) 'a is 1'
        case(2:20)
            write(*,*) 'a is between 2 and 20'
        case default
            write(*,*) 'a is not between 1 and 20'
    end select


    do j=1,20
        if((j>=1).and.(j<=5)) then
            print *, j
        else if(j<15) then
            print *, 'j>5'
        else if(j==15) then
            exit
        end if
!        select case(j)
!            case(1:5)
!                print*, j
!            case(6:14)
!                print*, 'j>5'
!            case(15)
!                exit
!        end select
    end do


    print*, '5.1: 1/sqrt(2)', 1/2**.5
    print*, '5.1: exp(x)sin^2(x)', exp(x)*sin(x)**2
    print*, '5.1: sqrt(x^2+y^2)', sqrt(x**2+y**2)
    print*, '5.1: |x-y|', abs(x-y)


    E = 1
    F = 1
    G = 1
    H = (/1,2,3,4,5,6,7,8,9,10/)
    print *, matmul(E,F)
    print *, matmul(transpose(E),E)
    print *, matmul(matmul(E,F),G)
    print *, dot_product(H,H)

    print *, 'maximum of array H: ', MAXVAL(H)
    print *, 'minimum of array H: ', MINVAL(H)
    print *, 'sum of array H: ', SUM(H)
    print *, 'product  of array H: ', PRODUCT(H)


contains

    ! --- Add your subroutines and functions here
    ! 
    ! subroutine mysub
    ! 
    ! end subroutine mysub

end program myfortran
