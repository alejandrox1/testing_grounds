! dynamic_simple_calc.f90
PROGRAM dynamic_simple_calc
    IMPLICIT NONE

    INTEGER                         :: elements
    REAL                            :: delta
    REAL, ALLOCATABLE, DIMENSION(:) :: abscissa
    REAL, ALLOCATABLE, DIMENSION(:) :: temperature
    INTEGER                         :: e

    ! Request inpt from user.
    PRINT "(A)", "Enter the number of elements: "
    READ *, elements
    delta = 1.0/elements

    ! Allocate arays.
    ALLOCATE(abscissa(0:elements))
    ALLOCATE(temperature(0:elements))

    ! Array construction.
    abscissa = [(delta*e, e=0, elements)]

    temperature = sin(abscissa)/2.0

    PRINT "(A)", "Absissa, Temperature"
    DO e=0, elements
        PRINT "(E15.6, 1X, E15.6)", abscissa(e), temperature(e)
    END DO

END PROGRAM dynamic_simple_calc
