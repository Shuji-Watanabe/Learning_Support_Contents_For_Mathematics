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
"""#### 定積分の問題"""

x, y = sy.symbols("x, y")
disp_columns1_1= st.columns([1,1])
tmp_index_str = "definite_integral"
Q_dict = tmp2_json[tmp_index_str]
f_tuple = tuple( set([Q_dict[key]["fun"]for key in Q_dict.keys()]))

# st.write(f_tuple)
with disp_columns1_1[0]:
    select_radio = st.radio("関数の設定方法",("選択","直接入力"))
with disp_columns1_1[1]:
    if select_radio=="直接入力":
        tmp_fun_str = st.text_input("関数を入力",value="x**2")
        tmp_ini_str = st.text_input("$x_i$の数を入力",value="-1")
        tmp_fin_str = st.text_input("$x_f$の数を入力",value="1")
        if tmp_fun_str and tmp_ini_str and tmp_fin_str:
            function_str= tmp_fun_str 
            x_ini_str = tmp_ini_str 
            x_fin_str = tmp_fin_str 
        else:
            st.warning("関数, $~x_i~$, $~x_f~$を入力してください")
            st.stop()
    elif select_radio=="選択":
        function_str=  st.selectbox("関数の選択",f_tuple)
        Integral_range= { key:value for key, value in Q_dict.items() if value["fun"] == function_str}
        if len(Integral_range) == 1 :
            tmp_keys = list(Integral_range.keys())[0]

        else :
            tmp_keys = list(Integral_range.keys())
            tmp_dict = {}
            for key in tmp_keys:
                x_ini,x_fin = Integral_range[key]["initial"],Integral_range[key]["final"]
                tmp_str = f"{x_ini} から {x_fin}"
                tmp_dict[tmp_str]=key 
            tmp_keys = tmp_dict[st.selectbox("使用する積分範囲を選択",tuple(tmp_dict.keys()))]
        function_str = Integral_range[tmp_keys]["fun"]
        x_ini_str = Integral_range[tmp_keys]["initial"]
        x_fin_str = Integral_range[tmp_keys]["final"]


function_sym = sy.sympify(function_str)
x_ini_sym = sy.sympify(x_ini_str)
x_fin_sym = sy.sympify( x_fin_str )

function_latex = sy.latex(function_sym)
x_ini_latex = sy.latex( x_ini_sym )
x_fin_latex = sy.latex(x_fin_sym )

definite_f_exper_sym = sy.Integral(function_sym,(x,x_ini_sym,x_fin_sym))
definite_f_expr_latex = sy.latex( definite_f_exper_sym)
definite_f_result_latex = sy.latex( definite_f_exper_sym.doit() )

indefinite_f_exper_sym  = sy.Integral(function_sym,x)
indefinite_f_result_exper_sym  = sy.Integral(function_sym,x).doit()
indefinite_f_result_exper_latex = sy.latex(indefinite_f_result_exper_sym )
st.write("入力情報")
f"""
    $$\\displaystyle 
        {definite_f_expr_latex } \
        = \\left[ \\phantom{{\\Big[}} {indefinite_f_result_exper_latex} \\phantom{{\\Big]}}  \\right]_{{{x_ini_latex}}}^{{{x_fin_latex}}}\
        = {definite_f_result_latex}
    $$
"""

# if st.checkbox("置換積分"):
#     disp_columns1_1_2 = st.columns([2,1,1])
#     with  disp_columns1_1_2[0]:
#         select_radio1_2 = st.radio( "置き換え方",("t=g(x)","作成中"),horizontal=True)
#     if select_radio1_2 == "t=g(x)":
#         with  disp_columns1_1_2[1]:
#             new_value = st.text_input("新しい変数",value="t")
#             new_value_sym = sy.Symbol(new_value)
#         with  disp_columns1_1_2[2]:
#             relation_str = st.text_input("$tと置き換える式$",value="3*x-1")
#             relation_sym = sy.sympify(relation_str)
#     Ans_f_def_new =definite_f_exper_sym.transform(relation_sym ,new_value_sym)
#     Ans_f_def_new_latex = sy.latex(Ans_f_def_new)
#     Ans_f_def_new_done = Ans_f_def_new.doit()
#     Ans_f_def_new_done_latex = sy.latex(Ans_f_def_new_done)


#     Ans_f_new_done = indefinite_f_exper_sym.transform(relation_sym ,new_value_sym)

#     Ans_f_replaced = Ans_f_new_done.replace(new_value_sym,relation_sym)
#     Ans_f_latex = sy.latex(Ans_f_replaced)
#     st.markdown(f"$\\displaystyle {definite_f_expr_latex }=\
#                 {Ans_f_def_new_latex  }=\
#                 = \\left[ \\phantom{{\\Big[}} {Ans_f_new_done} \\phantom{{\\Big]}}  \\right]_{{{x_ini_latex}}}^{{{x_fin_latex}}}\
#                 = { Ans_f_def_new_latex }$")
    # with st.expander("Latex コード(デフォルト)"):
    #     st.write("\"",Ans_f_latex,"+C\"")


# if st.checkbox("計算結果の表示変更"):
#     disp_columns1_2_1 = st.columns([2,1])
#     select_radio2 = st.radio( "結果の変更",("簡略化","展開","因数分解","その他"),horizontal=True)
#     st.write("積分後の関数(簡略化)")
#     if select_radio2 == "簡略化":
#         Ans_f_simplify = sy.simplify(indefinite_f_exper_sym ,force=True)
#     elif select_radio2 == "展開":
#         Ans_f_simplify = sy.expand(indefinite_f_exper_sym )
#     elif select_radio2 == "因数分解":
#         Ans_f_simplify = sy.factor(indefinite_f_exper_sym )
#     elif select_radio2 == "その他":
#         Ans_f_simplify = sy.powsimp(indefinite_f_exper_sym )

#     Ans_f_simplify_latex = sy.latex(Ans_f_simplify) 

#     st.markdown(f"$\\displaystyle {indefinite_f_result_exper_latex }={Ans_f_simplify_latex }+C$")
#     with st.expander("Latex コード(簡略化)"):
#         st.write("\"",Ans_f_simplify_latex,"+C\"")

"""---"""

