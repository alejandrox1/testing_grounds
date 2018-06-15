! simple_calc.f90
PROGRAM simple_calc
    IMPLICIT NONE

    INTEGER, PARAMETER             :: elements=10
    REAL,    PARAMETER             :: delta=1.0/elements
    REAL,    DIMENSION(0:elements) :: abscissa
    REAL,    DIMENSION(0:elements) :: temperature
    INTEGER                        :: e

    ! Array constructor.
    abscissa = [(delta*e, e=0, elements)]

    temperature = sin(abscissa)/2.0

    PRINT "(A)", "Absissa, Temperature"
    DO e=0, elements
        PRINT "(E15.6, 1X, E15.6)", abscissa(e), temperature(e)
    END DO

END PROGRAM simple_calc
