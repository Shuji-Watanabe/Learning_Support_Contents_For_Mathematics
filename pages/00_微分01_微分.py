import streamlit as st
import pandas as pd
import os
import sys
path = os.getcwd()


import sympy as sym
import random   
from librarys import disp_f
from librarys import differential



import json
tmp_data = open("pages/data_file.json")
data_json = json.load(tmp_data)

# Q1 -------
"""#### 微分の問題"""
f_dict = data_json["differential_calculus"]
f_dict_keys_list = f_dict.keys()
tmp_f_dict = { f_dict[qnum]:qnum for qnum in f_dict_keys_list}
f_tuple = tuple(tmp_f_dict.keys())


disp_columns1_1= st.columns([1,1])
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
        function_str=  st.selectbox("関数の選択",f_tuple)

fun_sym = sym.sympify(function_str)
fun_latex = sym.latex(fun_sym)
Ans_f, Ans_f_latex = differential.diff_one_val(fun_sym,"x")

Ans_f_latex =Ans_f_latex.replace("\\log{\\left(e \\right)}","")
Ans_f_latex_simp = sym.latex(sym.factor(sym.simplify(Ans_f,force=True)))
Ans_f_latex_simp =Ans_f_latex_simp.replace("\\log{\\left(e \\right)}","")

f"""
#### 問題  
次の関数を$~x~$で微分しなさい．  
$$
f(x) = {fun_latex}
$$
"""
with st.expander("答え"):
    st.write("微分後の関数")
    st.markdown(f"$\\displaystyle f'(x)={Ans_f_latex}$")
    st.markdown(f"簡略化$\\displaystyle f'(x)={Ans_f_latex_simp}$")
"""---"""

