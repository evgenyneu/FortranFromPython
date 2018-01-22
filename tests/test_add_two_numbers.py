from ..fortran import add_two_numbers

def test_add_two_numbers():
    """
    Test a fortran function from fortran/add_two_numbers.f90.

    In order to build an extension module for python, cd to fortran and run

        f2py -c -m add_two_numbers add_two_numbers.f90
    """
    assert add_two_numbers.add(3,7) == 10