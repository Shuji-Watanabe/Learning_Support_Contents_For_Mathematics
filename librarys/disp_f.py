import sympy as sym
from sympy.abc import x, y

def format_disp(expr_str):
    """
    expr_str : expression in sympy form
    return : expr_str_sympy,expr_str_latex
    """
    expr_str_sympy = sym.sympify(expr_str)
    expr_str_latex  = sym.latex(expr_str_sympy )
    return expr_str_sympy,expr_str_latex