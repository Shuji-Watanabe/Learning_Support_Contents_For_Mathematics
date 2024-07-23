import streamlit as st
import pandas as pd
import os
import sys
path = os.getcwd()


import sympy as sym
import random   
from librarys import disp_f
from librarys import differential



# Q1 -------
"""#### 微分の問題"""
disp_columns1_1= st.columns([1,1])
f_01_list = ["cos(x)","log(x,3)","e**x",\
             "2*x-1/(2*x)","sin(2*x-pi/4)","1-2*sqrt(x-1)",\
             "e**x*sin(x)","(x**2-2*x)/(x**3+1)","sin(x**2)",\
             "(1-x**2)**(1/3)","e**(-2*x)","x*sqrt(x)"]
f_01_tuple = tuple(f_01_list)
with disp_columns1_1[0]:
    select_radio = st.radio("関数の設定方法",("選択","直接入力"))
with disp_columns1_1[1]:
    if select_radio=="直接入力":
        tmp_str = st.text_input("関数を入力",value="x**2*e**x")
        if tmp_str:
            function_str= tmp_str
        else:
            st.warning("関数を入力してください")
            st.stop()
    elif select_radio=="選択":
        function_str=  st.selectbox("関数の選択",f_01_tuple)

fun_sym = sym.sympify(function_str)
fun_latex = sym.latex(fun_sym)
Ans_f, Ans_f_latex = differential.diff_one_val(fun_sym,"x")

Ans_f_latex =Ans_f_latex.replace("\\log{\\left(e \\right)}","")
Ans_f_latex_simp = sym.latex(sym.factor(sym.simplify(Ans_f,force=True)))
Ans_f_latex_simp =Ans_f_latex_simp.replace("\\log{\\left(e \\right)}","")
disp_columns1_2= st.columns([1,1])
with disp_columns1_2[0]:
    st.write("微分前の関数　")
    st.markdown(f"$\\displaystyle\\ f(x)={fun_latex}$")
    with st.expander("Latex コード"):
        st.write("\"",fun_latex,"\"")

with disp_columns1_2[1]:
    st.write("微分後の関数")
    st.markdown(f"$\\displaystyle f'(x)={Ans_f_latex}$")
    with st.expander("Latex コード(デフォルト)"):
        st.write("\"",Ans_f_latex,"\"")
    st.markdown(f"簡略化$\\displaystyle f'(x)={Ans_f_latex_simp}$")
    with st.expander("Latex コード(簡略化)"):
        st.write("\"",Ans_f_latex_simp,"\"")
"""---"""

