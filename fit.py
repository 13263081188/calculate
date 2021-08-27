import streamlit as st
import numpy as np
from bokeh.plotting import figure,show
import matplotlib.pyplot as plt
import pandas as pd
x = np.array([-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])
y = np.array(2*(x**4) + x**2 + 9*x + 2) #假设因变量y刚好符合该公式
#y = np.array([300,500,0,-10,0,20,200,300,1000,800,4000,5000,10000,9000,22000])
def main():
    # Wide mode
    st.set_page_config(layout="wide", page_title="计算机配色")
    st.write('\n')
    st.write("结果展示")

    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    p = figure(
    title = 'simple line example',
    x_axis_label = 'x',
    y_axis_label = 'y')
    # st.write(p)
    p.line(x, y, legend_label='Trend', line_color = 'red', line_width=1)

    # coef 为系数，poly_fit 拟合函数
    coef1 = np.polyfit(x,y, 1)
    poly_fit1 = np.poly1d(coef1)
    p.line(x, poly_fit1(x), legend_label='coef1', line_color='blue', line_width=1)

    coef2 = np.polyfit(x,y, 2)
    poly_fit2 = np.poly1d(coef2)
    p.line(x, poly_fit2(x), legend_label='coef2', line_color='black', line_width=1)
    # st.plot(x, poly_fit2(x), 'b',label="二阶拟合")

    coef3 = np.polyfit(x,y, 3)
    poly_fit3 = np.poly1d(coef3)
    p.line(x, poly_fit3(x), legend_label='coef3', line_color='green', line_width=1)
    # st.plot(x, poly_fit3(x), 'y',label="三阶拟合")
    # print(poly_fit3)

    coef4 = np.polyfit(x,y, 4)
    poly_fit4 = np.poly1d(coef4)
    p.line(x, poly_fit4(x), legend_label='coef4', line_color='orange', line_width=1)

    coef5 = np.polyfit(x,y, 5)
    poly_fit5 = np.poly1d(coef5)
    p.line(x, poly_fit5(x), legend_label='coef5', line_color='yellow', line_width=1)

    #
    # st.scatter(x, y, color='black')
    # st.legend(loc=2)
    # plt.show()
    #
    #
    # st.line_chart(chart_data)
    st.write("ending")
    st.bokeh_chart(p, use_container_width=True)
    show(p)
    st.write("cooling-ing")
if __name__ == '__main__':
    main()
