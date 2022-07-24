#!/usr/bin/python3
"""
    This modules defines function to divide a matrix by a number
"""


def is_list(l):
    """Check if an element is of list type
    Raises:
        TypeError: if its not a list type
    """

    if type(l) != list or l == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


def div_number(num, div):
    """Divide a number by a divisor"""

    if type(num) != int and type(num) != float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return round((num / div), 2)


def matrix_divided(matrix, div):
    """Divides a mtrix by a num
    Args:
        matrix: the matrix to divide
        div: number to divide matrix with

    Raises:
        TypeError: if `div` is not a number
                   if `matrix` is empty or not a list of list of integers/ float
                   if length of row is not constant
        ZeroDivisionError: if `div` is equal to zero

    Return:
        new divided matrix
    """

    is_list(matrix)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    is_list(matrix[0])
    row_length = len(matrix[0])

    new_list = []
    for row in matrix:
        is_list(row)
        if (len(row) != row_length):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = [div_number(elem, div) for elem in row]
        new_list.append(new_row)
    
    return new_list
