import sympy as sym
from sympy import sin, cos, Function, diff
from sympy.abc import x, y


def diff_one_val(function,variable):
    val = sym.Symbol(variable)
    input_function = sym.sympify(function)
    d_function = sym.diff(input_function,val)
    d_function_latex = sym.latex(d_function)
    return d_function,d_function_latex