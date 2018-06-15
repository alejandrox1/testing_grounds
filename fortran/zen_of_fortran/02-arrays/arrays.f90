! arrays.f90
PROGRAM arrays
    IMPLICIT NONE

    INTEGER, PARAMETER                :: rows=5
    INTEGER, PARAMETER                :: columns=3
    INTEGER, DIMENSION(rows, columns) :: array
    INTEGER                           :: c
    INTEGER                           :: r
    INTEGER                           :: x=0

    DO c=1, columns
        DO r=1, rows
            array(r,c) = x
            x = x + 1
        END DO
    END DO

    DO c=1, columns
        DO r=1, rows
            PRINT*, array(r,c) ! right column-major memory access.
        END DO
    END DO

END PROGRAM arrays
