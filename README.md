# Running a Fortran function from Python

This example shows how to run a Fortran function from Python.


## Setup

Install `scipy` package. It includes the `f2py` utility that we will use.

```
pip3 install scipy
```

Install `pytest` to run the unit tests:

```
pip3 install pytest
```

Clone this repository.

```
git clone https://github.com/evgenyneu/FortranFromPython.git
cd FortranFromPython
```

## Fortran function

We have a simple Fortran function that receives two integer numbers and returns their sum. Our goal is to run this function from Python.

```Fortran
function add(a, b) result(result)
    integer     :: a
    integer     :: b
    integer     :: result
    result = a + b
end function add
```

## Generate Python module from Fortran code

Change to the `fortran` directory and build a Python extension module:

```
f2py -c -m add_two_numbers add_two_numbers.f90
```

## Run Fortran code from Python

It will generate a module file. To check that it is working, open python console from the `fortran` directory:


```
python3
>>> import add_two_numbers
>>> add_two_numbers.add(1,41)
42
```

## Run Fortran code from a unit test

The Fortran code is also executed from the unit test. To run the test, run `pytest` from the root directory.

## Reference

* [Using Python as glue](https://docs.scipy.org/doc/numpy-1.10.0/user/c-info.python-as-glue.html)

