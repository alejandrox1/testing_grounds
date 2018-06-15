FC=gfortran

.PHONY: arrays clean

arrays: arrays.f90
	$(FC) -o $@ $^

clean:
	rm -f arrays
	rm -f *.mod
