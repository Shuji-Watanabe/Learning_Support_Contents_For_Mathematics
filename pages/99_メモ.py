

#Old version
# f_01_list = ["cos(x)","log(x,3)","e**x",\
#              "2*x-1/(2*x)","sin(2*x-pi/4)","1-2*sqrt(x-1)",\
#              "e**x*sin(x)","(x**2-2*x)/(x**3+1)","sin(x**2)",\
#              "(1-x**2)**(1/3)","e**(-2*x)","x*sqrt(x)"]
# f_01_df = pd.DataFrame(f_01_list ,columns=["関数"],)
# edited_df = st.data_editor(f_01_df)
# f_01_list = edited_df["関数"].values.tolist()

# count_01 = 0
# disp_columns= st.columns([1,2,2])
# with disp_columns[0]: 
#     Q_number = int(st.number_input("問題番号-1",step=1))
#     fun = f_01_list[Q_number ]
#     fun_sym = sym.sympify(fun)
#     fun_latex = sym.latex(fun_sym)
#     Ans_f, Ans_f_latex = differential.diff_one_val(fun,"x")
#     Ans_f_latex_simp = sym.latex(sym.factor(sym.simplify(Ans_f,force=True)))

# with disp_columns[1]:
#     st.markdown(f"$({1+f_01_list.index(fun)})\\ f(x)={fun_latex}$")
#     st.write("\"",fun_latex,"\"")

# with disp_columns[2]:
#     st.markdown(f"$({1+f_01_list.index(fun)})\\ f'(x)={Ans_f_latex}$")
#     st.markdown(f"$({1+f_01_list.index(fun)})\\ f'(x)={Ans_f_latex_simp}$")
#     st.write("\"",Ans_f_latex,"\"")
#     st.write("\"",Ans_f_latex_simp,"\"")



#Old version
# # Q2 -------
# """#### 和の計算"""

# expr = 'S = c_0\cdot \\sum_{k=1}^N 1\
#         + c_1\\cdot \\sum_{k=1}^N k\
#         + c_2\cdot \\sum_{k=1}^N k^2\
#         + c_3\cdot\\sum_{k=1}^N  k^3'
# f"""$\\displaystyle {expr}$"""
# coff = [""]*4
# disp_columns = st.columns([1]*5)
# with disp_columns[0]:
#     n_end = st.text_input("$\\ N\\ $の値","n")
# with disp_columns[1]:
#     coff[0] = st.text_input("$\\ c_0\\ $の値","1")
# with disp_columns[2]:
#     coff[1] = st.text_input("$\\ c_1\\ $の値","1")
# with disp_columns[3]:
#     coff[2] = st.text_input("$\\ c_2\\ $の値","1")
# with disp_columns[4]:
#     coff[3] = st.text_input("$\\ c_3\\ $の値","1")
# expr = expr.replace("N",n_end)
# for tmp_coff in coff:
#     expr = expr.replace(f"c_{coff.index(tmp_coff)}",tmp_coff)

# f"""#### 入力される式\n\n
# $$ \\displaystyle {expr}$$
# """

# try :
#     n,k = sym.symbols(f'{n_end},k')
# except:
#     st.write("$~N~$を別な文字にしてください．")

# n_end_sym = sym.sympify(n_end)
# coff_sym = sym.sympify(coff)

# expr_sym_list=[""]*4
# expr_sym_list[0] = sym.factor(coff_sym[0]*sym.summation(1, (k, 1, n_end_sym)))
# expr_sym_list[1] = sym.factor(coff_sym[0]*sym.summation(k, (k, 1, n_end_sym)))
# expr_sym_list[2] = sym.factor(coff_sym[0]*sym.summation(k**2, (k, 1, n_end_sym)))
# expr_sym_list[3] = sym.factor(coff_sym[0]*sym.summation(k**3, (k, 1, n_end_sym)))

# for i in range(len(expr_sym_list)):
#     st.markdown(f"第{i+1}項$\\ :\\ \\displaystyle {sym.latex( expr_sym_list[i])}$")