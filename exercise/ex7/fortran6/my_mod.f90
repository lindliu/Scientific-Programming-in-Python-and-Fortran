module my_mod

    implicit none

    ! --- Variable declarations here

contains

    ! --- Subroutine and function declarations here
    subroutine fun6_1(x, out)
        real :: x
        real :: out

        out = exp(x)*sin(x)**2
    end subroutine

    subroutine fun6_2(data, n, mean, var)
        real, dimension(:) :: data
        integer :: n
        real :: mean, var

        if (n<=1) then
            print *, 'data should has more than one element'
            stop
        end if

        mean = SUM(data)/n
        var = SUM((data-mean)**2)/(n-1)
    end subroutine
end module my_mod
