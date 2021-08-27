import streamlit as st
import numpy as np
from bokeh.plotting import figure,show
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['axes.unicode_minus']=False
import pandas as pd
x = np.array([i for i in range(10000)])
y = np.array(2*(x**4) + x**2 + 9*x + 2) #假设因变量y刚好符合该公式
#y = np.array([300,500,0,-10,0,20,200,300,1000,800,4000,5000,10000,9000,22000])
color_ = ['black','red','green','orange','yellow','blue']
def main():
    # Wide mode
    st.set_page_config(layout="wide", page_title="单位浓度k/s值计算")
    st.sidebar.title("设置输入组数")
    number = st.sidebar.text_input("组数")
    st.write('\n')
    st.write("输入")
    if number:
        col_form_input_x = [0 for _ in range(int(number))]
        col_form_input_y = [0 for _ in range(int(number))]
        col = st.columns(int(number))
        col_form = [col[_].form(key=str(_)) for _ in range(int(number))]
        col_form_c = [[] for _ in range(int(number))]
        for i in range(int(number)):
            col_form_input_x[i] = col_form[i].text_input("浓度")
            col_form_input_y[i] = col_form[i].text_input("k/s值")
            if col_form[i].form_submit_button("确认"):
                # st.write(col_form_input_x)
                pass
        st.write("输入对应浓度和选择的拟合多项式阶数")
        z = st.form(key="input_")
        c_ = (z.text_input("对应浓度"))
        poly_ = (z.text_input("选择模拟多项式的阶数"))
        if z.form_submit_button("确认"):
            st.write("请点击可视化分析显示结果》》》")
        if st.button("可视化分析") and c_ and poly_:
            x = [float(j) for j in col_form_input_x]
            y = [float(j) for j in col_form_input_y]

            fig, ax = plt.subplots()
            matplotlib.rcParams['font.family'] = 'SimHei'  # 字体设置为黑体
            plt.xlabel('浓度')
            plt.ylabel('k/s值')
            plt.title('k/s值随浓度变化')
            #origin
            ax.plot(x, y, label='原始数据', linewidth=1, color='black', marker='o',
                    markerfacecolor='black', markersize=2)
            import  collections
            polyder = collections.defaultdict(np.poly1d)
            poly_fit = collections.defaultdict(np.poly1d)
            for i in range(1, 6):
                poly_fit['poly_fit'+str(i)] = np.poly1d(np.polyfit(x,y,i))
                ax.plot(x,poly_fit['poly_fit'+str(i)](x),label = 'coef'+str(i), color = color_[i],linewidth = i)
            for i in range(1,6):
                # st.write("coef"+str(i),eval("coef"+str(i)))
                polyder["polyder"+str(i)] = np.polyder(poly_fit["poly_fit"+str(i)])
                # st.write(np.polyder(eval("poly_fit"+str(i)))(x))
            plt.legend()
            st.pyplot(fig)
            fig1, ax1 = plt.subplots()

            matplotlib.rcParams['font.family'] = 'SimHei'  # 字体设置为黑体
            plt.xlabel('浓度')
            plt.ylabel('单位浓度k/s')
            plt.title('单位浓度k/s值随浓度变化')
            for i in range(1,6):

                ax1.plot(x, polyder["polyder"+str(i)](x), label=str(i)+"阶多项式单位浓度k/s", linewidth=1, color=color_[i])
                # st.write(i)
            plt.legend()
            st.pyplot(fig1)
            st.sidebar.write("单位浓度k/s结果：")
            st.sidebar.write(str(polyder["polyder"+str(poly_)](float(c_))))
if __name__ == '__main__':
    main()
