! modular.f90
MODULE echoer
CONTAINS
    SUBROUTINE say_something(what)
        CHARACTER(*), INTENT(IN) :: what
        PRINT '(A)', what
    END SUBROUTINE say_something
END MODULE echoer

PROGRAM echoer_program
    USE echoer
    CALL say_something(what='Hello modular world, this is Fortran!')
END PROGRAM echoer_program
