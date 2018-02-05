# Running a Fortran function from Python

This example shows how to run a Fortran function from Python.


## Setup

Install `scipy` package. It includes the `f2py` utility that we will use.

```
pip3 install scipy
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

## Verify f2py utility version

You've installed `scipy` package that includes the `f2py`. There are two incompatible versions of Python: Python2 and Python3. We need to make sure that when we type `f2py` command it executes the Python3 version of this utility.

```
which f2py
```

It will show the location of the utility, usually something like

```
/Library/Frameworks/Python.framework/Versions/3.6/bin/f2py
```

You can see that utility belongs to Python 3.6, which means we use the correct one. If the returned location corresponds to Python 2, then you will need to look at your `.bash_profile` (on Mac) and add Python3 binaries directory to the PATH variable.


## Generate Python module from Fortran code

Change to the `fortran` directory of this repository and build a Python extension module:

```
f2py -c -m add_two_numbers add_two_numbers.f90
```

## Run Fortran code from Python

The `f2py` utility will generate a module file that can be imported into Python code. To check that it is working, open python console from the `fortran` directory:


```
python3
>>> import add_two_numbers
>>> add_two_numbers.add(1,41)
42
```

## Run Fortran code from a unit test

The Fortran code is also executed from the unit test.

Install `pytest`:

```
pip3 install pytest
```

From the root directory of this repository, run

```
pytest
```

## Reference

* [Using Python as glue](https://docs.scipy.org/doc/numpy-1.10.0/user/c-info.python-as-glue.html)

