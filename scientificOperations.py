import math


def scientific_calculate(operation, num1):
    """
    Performs the given scientific operation on the given number, which may be either an integer or a float.

    args:
        - operation: the operation to perform (sin, cos, tan, ln)
        - num1: the number to perform the operation on

    returns:
        - the result of the operation on the given number
    """

    if operation == 'sin':
        return math.sin(num1)

    elif operation == 'cos':
        # Calculate the cosine
        cosine = math.cos(num1)
        # Return the cosine
        return cosine

    elif operation == 'tan':
        # Calculate the tangent
        tangent = math.tan(num1)
        # Return the tangent
        return tangent

    elif operation == 'ln':
        # Calculate the natural log
        natLog = math.log(num1)
        # Return the natural log of num1
        natlog = math.log(num1)

    else:
        raise ValueError(
            'Invalid Operation: Scientific Operations are (sin, cos, tan, ln, sqrt, !, ^, and %)')
