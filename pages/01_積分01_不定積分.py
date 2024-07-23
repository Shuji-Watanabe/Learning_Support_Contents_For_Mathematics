import streamlit as st
import sympy as sy
import os
import sys
path = os.getcwd()

from librarys import disp_f
from librarys import differential

import json
tmp_qlist =open("pages/data_file.json")
tmp2_json = json.load(tmp_qlist )

# Q1 -------
"""#### 不定積分の問題"""

x, y = sy.symbols("x, y")
disp_columns1_1= st.columns([1,1])

tmp_index_str = "indefinite_integral"
f_01_list = [ tmp2_json[tmp_index_str][i] for i in tmp2_json[tmp_index_str].keys() ] 


f_01_tuple = tuple(f_01_list)
with disp_columns1_1[0]:
    select_radio = st.radio("関数の設定方法",("選択","直接入力"))
with disp_columns1_1[1]:
    if select_radio=="直接入力":
        tmp_str = st.text_input("関数を入力",value="(3*x**5+2*x**2)/x**2")
        if tmp_str:
            function_str= tmp_str
        else:
            st.warning("関数を入力してください")
            st.stop()
    elif select_radio=="選択":
        function_str=  st.selectbox("関数の選択",f_01_tuple)


fun_sym = sy.sympify(function_str)
fun_latex = sy.latex(fun_sym)
st.write("積分前の関数　")
st.markdown(f"$\\displaystyle\\ f(x)={fun_latex}$")
with st.expander("Latex コード"):
    st.write("\"",fun_latex,"\"")

st.write("積分後の関数(デフォルト)")
Ans_f_form = sy.Integral(fun_sym,x) 
Ans_f_form_latex = sy.latex(Ans_f_form).replace("\\log{\\left(e \\right)}","")

Ans_f = Ans_f_form.doit()
Ans_f_latex = sy.latex(Ans_f).replace("\\log{\\left(e \\right)}","")
st.markdown(f"$\\displaystyle {Ans_f_form_latex }={Ans_f_latex}+C$")
with st.expander("Latex コード(デフォルト)"):
    st.write("\"",Ans_f_latex,"+C\"")

if st.checkbox("置換積分"):
    disp_columns1_1_2 = st.columns([2,1,1])
    with  disp_columns1_1_2[0]:
        select_radio1_2 = st.radio( "置き換え方",("t=g(x)","作成中"),horizontal=True)
    if select_radio1_2 == "t=g(x)":
        with  disp_columns1_1_2[1]:
            new_value = st.text_input("新しい変数",value="t")
            new_value_sym = sy.Symbol(new_value)
        with  disp_columns1_1_2[2]:
            relation_str = st.text_input("$tと置き換える式$",value="3*x-1")
            relation_sym = sy.sympify(relation_str)
    Ans_f_new = Ans_f_form.transform(relation_sym ,new_value_sym)
    Ans_f_new_latex = sy.latex(Ans_f_new).replace("\\log{\\left(e \\right)}","")
    Ans_f_new_done = Ans_f_new.doit()
    Ans_f_new_done_latex = sy.latex(Ans_f_new_done).replace("\\log{\\left(e \\right)}","")
    Ans_f_replaced = Ans_f_new_done.replace(new_value_sym,relation_sym)
    Ans_f_latex = sy.latex(Ans_f_replaced).replace("\\log{\\left(e \\right)}","")
    st.markdown(f"$\\displaystyle {Ans_f_form_latex }={Ans_f_new_latex  }={Ans_f_new_done_latex }={Ans_f_latex}+C$")
    with st.expander("Latex コード(デフォルト)"):
        st.write("\"",Ans_f_latex,"+C\"")


if st.checkbox("計算結果の表示変更"):
    disp_columns1_2_1 = st.columns([2,1])
    select_radio2 = st.radio( "結果の変更",("簡略化","展開","因数分解","その他"),horizontal=True)
    st.write("積分後の関数(簡略化)")
    if select_radio2 == "簡略化":
        Ans_f_simplify = sy.simplify(Ans_f,force=True)
    elif select_radio2 == "展開":
        Ans_f_simplify = sy.expand(Ans_f)
    elif select_radio2 == "因数分解":
        Ans_f_simplify = sy.factor(Ans_f)
    elif select_radio2 == "その他":
        Ans_f_simplify = sy.powsimp(Ans_f)

    Ans_f_simplify_latex = sy.latex(Ans_f_simplify).replace("\\log{\\left(e \\right)}","")

    st.markdown(f"$\\displaystyle {Ans_f_form_latex }={Ans_f_simplify_latex }+C$")
    with st.expander("Latex コード(簡略化)"):
        st.write("\"",Ans_f_simplify_latex,"+C\"")

"""---"""

