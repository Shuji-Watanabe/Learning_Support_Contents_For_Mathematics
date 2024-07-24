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

# Q -------
"""#### 総和の問題"""
x, y= sy.symbols("x y")
k= sy.Symbol("k")
n= sy.Symbol("n",real=True, positive=True)
# n, m = sy.symbols("n, m",real=True, positive=True,nonzero=True,finite=True)


tmp_index_str = "summation"
ak_01_list =  [ tmp2_json[tmp_index_str][i] for i in tmp2_json[tmp_index_str].keys() ] 


disp_columns1_1= st.columns([1,1])
ak_01_tuple = tuple(ak_01_list)
with disp_columns1_1[0]:
    select_radio = st.radio("数列の設定方法",("選択","直接入力"))
with disp_columns1_1[1]:
    if select_radio=="直接入力":
        tmp_str = st.text_input("数列を入力",value="2*k+3*k**2")
        if tmp_str:
             ak_str= tmp_str
        else:
            st.warning("第$~k~$項の式を正しく入力してください")
            st.stop()
    elif select_radio=="選択":
        ak_str= st.selectbox("数列の選択",ak_01_tuple)

ak_sym = sy.sympify(ak_str).subs("n",n).subs("k",k)
ak_latex = sy.latex(ak_sym)
sum_ak_sym = sy.summation(ak_sym, (k, 1, n))
sum_ak_latex = sy.latex(sy.factor(sum_ak_sym))

f"""
#### 問題  
次の和を求めなさい．
$$\\displaysytle 
 \\displaystyle \\sum_{{k=1}}^{{n}} \\left\\{{ {ak_latex}  \\right \\}} 
$$
"""
""""""

with st.expander("答え"):
    f"""
    $$
    \\displaystyle {sum_ak_latex }
    $$
    """

    if st.checkbox("途中計算の表示") :
        disp_columns2_1 = st.columns([1,4])

        ak_sym_expand = sy.expand(ak_sym,power_exp=True )
        ak_sym_expand_latex = sy.latex(ak_sym_expand)

        poly_degree = sy.poly(ak_sym_expand).degree()
        tmp_expr= 0
        coeff = [0]*(poly_degree+1) 
        for num in range(1+sy.poly(ak_sym_expand).degree()):
            coeff[num] = sy.diff(ak_sym_expand,k,num).subs(k, 0)/sy.factorial(num)
            tmp_expr += sy.factor(coeff[num]*sy.summation(sy.Pow(k,num), (k, 1, n)))

        tmp_expr_expand = sy.expand(tmp_expr,n, power_base=True, force=True)
        tmp_expr_expand_latex = sy.latex(tmp_expr_expand)   
        tmp_expr_latex = sy.latex(tmp_expr)
        
        st.write("途中式：$a_k~$の展開")
        f"""
        $$
            \\displaystyle a_k = {ak_latex} ={ak_sym_expand_latex}
        $$
        """

        st.write("等価な答え")
        tmp_radio = st.radio("答えの表示の変更",("公式代入直後","因数分解","展開"),horizontal=True)

        if tmp_radio == "公式代入直後":
            disp_expr = f"\\sum_{{k=1}}^{{n}} \\left\\{{  {ak_sym_expand_latex}\\right\\}}  ={tmp_expr_latex}"
        elif tmp_radio =="因数分解":
            disp_expr = f"\\sum_{{k=1}}^{{n}} \\left\\{{  {ak_sym_expand_latex}\\right\\}}  ={sum_ak_latex}"
        elif tmp_radio =="展開":
            disp_expr = f"\\sum_{{k=1}}^{{n}} \\left\\{{  {ak_sym_expand_latex}\\right\\}}  ={tmp_expr_expand_latex}"
    
        f"""
        $$
            \\displaystyle {disp_expr}
        $$
        """