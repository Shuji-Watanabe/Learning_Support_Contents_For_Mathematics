import streamlit as st
import pandas as pd
import os
import sys
path = os.getcwd()


import sympy as sym
import random   
from librarys import disp_f
from librarys import differential



# Q2 -------
x, y =sym.symbols("x y")

"""#### 接線&法線の問題"""
disp_columns2= st.columns([1,1])

with disp_columns2[0]:
    function_str = st.text_input("関数を入力","x**2")
with disp_columns2[1]:
    x_str = st.text_input("接点の$~x~$座標","2")

fun = function_str
fun_sym = sym.sympify(fun) ; fun_latex = sym.latex(fun_sym)
x_sym   = sym.sympify(x_str) ; x_latex = sym.latex(x_sym)

Ans_f, Ans_f_latex = differential.diff_one_val(fun_sym,"x")
Ans_f_latex_simp = sym.latex(sym.factor(sym.simplify(Ans_f,force=True)))

y_eq_sym = y-fun_sym.subs(x,x_sym)
y_eq_latex = sym.latex(y_eq_sym)
x_eq_sym = x-x_sym
x_eq_latex = sym.latex(x_eq_sym)

tline_slope_sym = Ans_f.subs(x,x_sym)
tline_slope_latex = sym.latex(tline_slope_sym)
nline_slope_sym = -1/Ans_f.subs(x,x_sym)
nline_slope_latex = sym.latex(nline_slope_sym)

t_line_sym = Ans_f.subs(x,x_sym)*(x-x_sym)+fun_sym.subs(x,x_sym )
t_line_latex = sym.latex(t_line_sym)

n_line_sym = -1/Ans_f.subs(x,x_sym)*(x-x_sym)+fun_sym.subs(x,x_sym )
n_line_latex = sym.latex(n_line_sym)

disp_columns2_2 = st.columns([2,3])
with disp_columns2_2[0]:
    st.write("**途中計算**")
    f"""
        - 関数$~f(x)~$の導関数  
            $$
            \\displaystyle f'(x)={Ans_f_latex}
            $$
        - $~x={sym.latex(x_sym)}~$における微分係数
            $$
            \\displaystyle f'({sym.latex(x_sym)})={sym.latex(Ans_f.subs(x,x_sym))}
            $$
        - 接点の座標
            $$
            \\displaystyle \\left({sym.latex(x_sym)},{sym.latex(fun_sym.subs(x,x_sym))} \\right)
            $$
    """
with disp_columns2_2[1]:
    st.write("**結論**")
    f"""
    - $f(x)={fun_latex}~$の$~x={x_sym}~$における接線の方程式
        $$
        \\displaystyle\
        {y_eq_latex}={tline_slope_latex}\\left({x_eq_latex}\\right)
        $$
        $$
        y={t_line_latex}
        $$
    - $f(x)={fun_latex}~$の$~x={x_sym}~$における法線の方程式
        $$
        \\displaystyle\
        {y_eq_latex}={nline_slope_latex}\\left({x_eq_latex}\\right)
        $$
        $$
        y={n_line_latex}
        $$
    """
"""---"""
