# Running Fortran code from Python

This is a collection of examples that show how to run Fortran code from Python.


## Setup

* Install `scipy` package that includes `f2spy`:

```
pip3 install scipy
```

* Install `pytest` to run the tests:

```
pip3 install pytest
```

## Generate Python module from fortran code

* Change to Fortran directory: `cd fortran`.

* Build a Python extension module from fortran code:

```
f2py -c -m add_two_numbers add_two_numbers.f90
```

## Run the unit test

The Fortran code is executed from the unit test. To run the test, enter from the root directory:

```
pytest
```

## Reference

* [Using Python as glue from scipy.org](https://docs.scipy.org/doc/numpy-1.10.0/user/c-info.python-as-glue.html)

