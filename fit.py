import streamlit as st
import numpy as np
from bokeh.plotting import figure
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
    p.line(x, y, legend_label='Trend', line_width=2)
    st.bokeh_chart(p, use_container_width=True)
    st.write("cooling-ing")
    # coef 为系数，poly_fit 拟合函数
    coef1 = np.polyfit(x,y, 1)
    poly_fit1 = np.poly1d(coef1)
    #
    # coef2 = np.polyfit(x,y, 2)
    # poly_fit2 = np.poly1d(coef2)
    # st.plot(x, poly_fit2(x), 'b',label="二阶拟合")
    # print(poly_fit2)
    #
    # coef3 = np.polyfit(x,y, 3)
    # poly_fit3 = np.poly1d(coef3)
    # st.plot(x, poly_fit3(x), 'y',label="三阶拟合")
    # print(poly_fit3)
    #
    # coef4 = np.polyfit(x,y, 4)
    # poly_fit4 = np.poly1d(coef4)
    # st.plot(x, poly_fit4(x), 'k',label="四阶拟合")
    # print(poly_fit4)
    #
    # coef5 = np.polyfit(x,y, 5)
    # poly_fit5 = np.poly1d(coef5)
    # st.plot(x, poly_fit5(x), 'r:',label="五阶拟合")
    # print(poly_fit5)
    #
    # st.scatter(x, y, color='black')
    # st.legend(loc=2)
    # plt.show()
    #
    #
    # st.line_chart(chart_data)
if __name__ == '__main__':
    main()
