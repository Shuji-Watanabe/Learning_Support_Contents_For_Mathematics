import streamlit as st
import pandas as pd
import os
import sys
path = os.getcwd()


import sympy as sy
import random   
from librarys import disp_f
from librarys import differential

import json
tmp_data = open("pages/data_file.json")
data_json = json.load(tmp_data)

# Q1 -------
"""#### 微分の問題"""
disp_columns1_1= st.columns([1,1])
f_dict = data_json["composition_function"]
f_dict_keys_list = f_dict.keys()
tmp_f_dict = { f_dict[qnum]["fun0"]:qnum for qnum in f_dict_keys_list}
f_tuple = tuple(tmp_f_dict.keys())
# st.write(f_tuple)

with disp_columns1_1[0]:
    select_radio = st.radio("関数の設定方法",("選択","直接入力"))
with disp_columns1_1[1]:
    if select_radio=="直接入力":
        tmp_set_columns1 = st.columns([3,1])
        with tmp_set_columns1[0]:
            tmp_str = st.text_input("関数を入力",value="e**(2*x-1)")
        with tmp_set_columns1[1]:        
            num_v_num = st.number_input("関数の数",value=2)

        if tmp_str:
            fun0= tmp_str
        else:
            st.warning("関数を入力してください")
            st.stop()

        tmp_set_columns2 = st.columns([1]*num_v_num)
        val_name = ["f","u"]
        init_funs= ["e**u","2*x-1"]
        tmp_str_vals = [""]*num_v_num
        for num_col in range(num_v_num ):
            with tmp_set_columns2[num_col]:
                tmp_str_vals[num_col] = st.text_input(f"${val_name[num_col]}=$",value=init_funs[num_col])
        if tmp_str_vals[0] and tmp_str_vals[1]:
            fun01,fun02 = tmp_str_vals[0], tmp_str_vals[1]
        else:
            st.warning("関数を入力してください")
            st.stop()
    elif select_radio=="選択":
        fun0=  st.selectbox("関数の選択",f_tuple)
        qnum = tmp_f_dict[fun0]
        fun01,fun02 = f_dict[qnum]["fun1"], f_dict[qnum]["fun2"]


fun0_latex = sy.latex(sy.sympify(fun0))
f"""
#### 次の関数を$~x~$で微分しなさい．  
$$
f(x) = {fun0_latex}
$$
"""

x, y, u, v = sy.symbols("x,y,u,v",real=True)

fun0_sym, fun1_sym, fun2_sym = sy.sympify(fun0),sy.sympify(fun01),sy.sympify(fun02)
fun1_sym = fun1_sym.subs("u",u)
fun2_sym = fun2_sym.subs("x",x)
fun1_org_sym = fun1_sym.subs(u,fun2_sym)

fun1_latex = sy.latex(fun1_sym)
fun2_latex = sy.latex(fun2_sym)

diff_fun1_sym = sy.diff(fun1_sym,u)
Ans_f1_sym = diff_fun1_sym
diff_fun2_sym = sy.diff(fun2_sym,x)
Ans_f_sym = Ans_f1_sym * diff_fun2_sym
Ans_f_sym =Ans_f_sym.subs(u,fun2_sym)


diff_fun1_latex = sy.latex(diff_fun1_sym)
diff_fun1_latex = diff_fun1_latex.replace("\\log{\\left(e \\right)}","")
diff_fun2_latex = sy.latex(diff_fun2_sym)
Ans_f_sy_latex = sy.latex(Ans_f_sym).replace("\\log{\\left(e \\right)}","")

with st.expander("答え"):
    f"""
        $$
        \\displaystyle
            \\frac{{dy}}{{dx}}\
            =\\frac{{d}}{{du}}\
                \\left\\{{ {fun1_latex} \\right\\}}\
                \\times\
                \\frac{{d}}{{dx}}\
                \\left\\{{ {fun2_latex} \\right\\}}\
            ={diff_fun1_latex} \\times {diff_fun2_latex}
            ={Ans_f_sy_latex}
        $$
    """

    """---"""

