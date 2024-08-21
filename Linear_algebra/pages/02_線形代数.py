import sympy as sy
import streamlit as st

Qfield_dict = {"内積":"dotp",\
                "外積":'crossp',\
                'なす角':'angle',\
                '面積':'area',\
                '直線の方程式':'eqofline',\
                '平面の方程式':'eqofplane',\
                '交点（直線と直線）':'intersec_line-line',\
                'End':'end'\
               }
Qfield_dict_keys = Qfield_dict.keys()
field_index = st.selectbox("計算項目",Qfield_dict_keys)

def input_vec(n_dim):
    colums_list01 = st.columns([2,1,1,2,2])
    vec_v = [2,-3,1] ; vec_u = [3,-1,-2] 
    with colums_list01[0]:
        dim_num = st.number_input("次元",value=n_dim,min_value=1,max_value=3)
        v_list = [0]*dim_num
        u_list = [0]*dim_num
    with colums_list01[1]:
        for i in range(dim_num):
            v_list[i] = st.text_input(f"$v_{i+1}$",f"{vec_v[i]}")
        v_sym=sy.Matrix(v_list)
    with colums_list01[2]:
        for i in range(dim_num):
            u_list[i] = st.text_input(f"$u_{i+1}$",f"{vec_u[i]}")
        u_sym=sy.Matrix(u_list)
    with colums_list01[3]:
        st.write("入力結果")
        st.markdown(f'Vector $~\mathbb{{v}}={sy.latex(v_sym)}~$')
    with colums_list01[4]:
        st.write("入力結果")
        st.markdown(f"Vector $~\mathbb{{u}}={sy.latex(u_sym)}~$")
    return dim_num,v_sym,u_sym

def input_point():
    init_points=[[4,-1,3],[5,2,0],[3,1,2]]
    dim_num = 3
    points=[[0,0,0],[0,0,0],[0,0,0]]
    colums_list01 = st.columns([1,1,1])
    for j in range(dim_num):
        with colums_list01[j]:
            for i in range(dim_num):
                # st.write(f"i={i}, j={j}")
                points[j][i] = st.text_input(f"$v_{{{j+1,i+1}}}$",f"{init_points[j][i]}",key=10*j+i)
    # st.write(points)
    for j in range(dim_num):
        with colums_list01[j]:
             p_sym=sy.Matrix(points)
             st.markdown(f"${{\\rm P}}_{j}={sy.latex(p_sym[j,:])}$")
    return dim_num, p_sym

def input_point_eql():
    init_points=[[0,1,2],[1,4,0]]
    dim_num = 3
    points=[[0,0,0],[0,0,0]]
    colums_list01 = st.columns([1,1])
    for j in range(2):
        with colums_list01[j]:
            for i in range(dim_num):
                # st.write(f"i={i}, j={j}")
                points[j][i] = st.text_input(f"$v_{{{j+1,i+1}}}$",f"{init_points[j][i]}",key=20*j+i)
    # st.write(points)
    for j in range(2):
        with colums_list01[j]:
             p_sym=sy.Matrix(points)
             st.markdown(f"${{\\rm P}}_{j}={sy.latex(p_sym[j,:])}$")
    return dim_num, p_sym



if Qfield_dict[field_index]=='crossp':
    f"""#### 外積"""
    dim_num,v_sym,u_sym = input_vec(n_dim=3)
    vxu = v_sym.cross(u_sym)
    """##### 各種計算結果"""
    st.markdown(f'Cross product $\\displaystyle ~{sy.latex(v_sym)} \\times{sy.latex(u_sym)} ={sy.latex(vxu)}~$')

elif Qfield_dict[field_index]=='angle':
    f"""#### 2つのベクトルのなす角度"""
    dim_num,v_sym,u_sym = input_vec(n_dim=3)
    norm_v=v_sym.norm()
    norm_u=u_sym.norm()
    vdotu = v_sym.dot(u_sym)
    cos_vu = vdotu/(norm_v*norm_u)
    theta = sy.acos(cos_vu)
    """##### 各種計算結果"""
    col01=st.columns([1,1])
    with col01[0]:
        st.markdown(f'$\\displaystyle ~ \\left\\|\\mathbf{{v}}\\right\\| ~=~ \\left\\|{sy.latex(v_sym)}\\right\\|={sy.latex(norm_v)}$')
        st.markdown(f'$\\displaystyle ~ \\left\\|\\mathbf{{u}}\\right\\| ~=~ \\left\\|{sy.latex(u_sym)}\\right\\|={sy.latex(norm_u)}$')
    with col01[1]:
        st.markdown(f"$~\\mathbf{{v}} \\cdot \\mathbf{{u}}~ = ~{sy.latex(vdotu)}$")
        st.markdown(f"$\\displaystyle  ~\\cos\\theta\
                                ~=~ \\frac{{\\mathbf{{v}} \\cdot \\mathbf{{u}}}}\
                                    {{ \\left\\|\\mathbf{{v}}\\right\\| \\left\\|\\mathbf{{u}}\\right\\|}} \
                                ~=~{sy.latex(cos_vu)}$")
        st.markdown(f"$\\displaystyle  ~\\theta\
                                ~=~ \\cos^{{-1}}\\left(\
                                                \\frac{{\\mathbf{{v}} \\cdot \\mathbf{{u}}}}\
                                                    {{ \\left\\|\\mathbf{{v}}\\right\\| \\left\\|\\mathbf{{u}}\\right\\|}}\
                                                \\right) \
                                ~=~{sy.latex(theta)}$")
    
elif Qfield_dict[field_index]=='area':
    f"""#### 2つのベクトルを辺に持つ平行四辺形，三角関数の面積"""
    dim_num, p_sym = input_point()
    
    """##### 各種計算結果"""
    col02=st.columns([2,1])
    v_1 = p_sym[1,:]-p_sym[0,:]
    v_2 = p_sym[2,:]-p_sym[0,:]
    v_1xv_2 =v_1.T.cross(v_2.T)
    S = v_1xv_2.norm()/2
    with col02[0]:
        st.markdown(f"$v_1 \
                    = \\overrightarrow{{P_1P_0}}\
                    = {sy.latex(p_sym[1,:].T)} - {sy.latex(p_sym[0,:].T)}\
                    = {sy.latex(v_1.T)}$")
        st.markdown(f"$v_2 \
                    = \\overrightarrow{{P_2P_0}}\
                    = {sy.latex(p_sym[2,:].T)} - {sy.latex(p_sym[0,:].T)}\
                    ={sy.latex(v_2.T)}$")
    with col02[1]:
        st.markdown(f"$v_1 \\times v_2 ={sy.latex(v_1xv_2)}$")
        st.markdown(f"$\\displaystyle S=\\frac{{1}}{{2}} \\|v_1 \\times v_2\\| = {sy.latex(S)}$")

elif Qfield_dict[field_index]=='eqofline':
    f"""#### 2点を通る直線の方程式"""
    dim_num, p_sym = input_point_eql()
    """##### 各種計算結果"""
    col03 = st.columns([1,1])
    v_1 = p_sym[1,:]-p_sym[0,:]
    with col03[0]:
        st.markdown(f"$v_1 \
                    = \\overrightarrow{{P_1P_0}}\
                    = {sy.latex(p_sym[1,:].T)} - {sy.latex(p_sym[0,:].T)}\
                    = {sy.latex(v_1.T)}$")
    with col03[1]:
        st.markdown(f"点$~\\rm P_0~$を通り$\\overrightarrow{{P_1P_0}}$に平行な直線の方程式")
        st.markdown(f"$$\\displaystyle\
                    \\frac{{x-\\left( {p_sym[0,0]} \\right)}} {{{v_1[0]}}} \
                    = \\frac{{y-\\left( {p_sym[0,1]} \\right)}} {{{v_1[1]}}} \
                    = \\frac{{z-\\left( {p_sym[0,2]} \\right)}} {{{v_1[2]}}} \
                    $$")


elif Qfield_dict[field_index]=='eqofplane':
    f"""#### 3点を通る平面の方程式"""
    dim_num, p_sym = input_point()
    """##### 各種計算結果"""
    col03 = st.columns([1,1])
    v_1 = p_sym[1,:]-p_sym[0,:]
    v_2 = p_sym[2,:]-p_sym[0,:]
    v_1xv_2 = v_1.cross(v_2)
    x,y,z = sy.symbols("x y z")
    r = sy.Matrix([x, y, z])
    v_3 = r-p_sym[0,:].T
    eq = v_1xv_2.dot(v_3)

    st.markdown(f"$ \\mathbf{{v}}_1 = \\overrightarrow{{P_0P_1}}={sy.latex(p_sym[1,:].T)} - {sy.latex(p_sym[0,:].T)} ={sy.latex(v_1.T)} $")
    st.markdown(f"$ \\mathbf{{v}}_2 = \\overrightarrow{{P_0P_2}}={sy.latex(p_sym[2,:].T)} - {sy.latex(p_sym[0,:].T)} ={sy.latex(v_2.T)} $")
    st.markdown(f"$ \\mathbf{{n}} = \\mathbf{{v}}_1 \\times \\mathbf{{v}}_2={sy.latex(v_1xv_2.T)}$")
    st.markdown(f"${sy.latex(eq)}=0$")

elif Qfield_dict[field_index]=='intersec_line-line':
    f"""#### 3点を通る平面の方程式"""
    dim_num, p_sym = input_point()
    """##### 各種計算結果"""