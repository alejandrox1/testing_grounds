FC=gfortran

.PHONY: arrays simple clean

arrays: arrays.f90
	$(FC) -o $@ $^

simple: simple_calc.f90
	$(FC) -o $@ $^

clean:
	rm -f arrays
	rm -f *.mod
