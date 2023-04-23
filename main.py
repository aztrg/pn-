import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot
from scipy import optimize as op
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
path='img'
if not os.path.exists(path):
    os.mkdir(path)
def sele():
    print('---------')
    print('0:结束')
    print('1:计算u1-u2曲线')
    print('2:计算u-t曲线')
def x_rays():#x轴
    x1=[x/100 for x in range(23,51,1)]
    x2=[x+273.15 for x in range(30,76,5)]
    return x1,x2
def curve_fit1(x,A,B):
    return A*2.71314**(B*x)
def curve_fit2(x,A,B):
    return A*x+B
def conver(data):
    list=[]
    for i in data:
        list.append(float(i))
    return list
'''數據示例y1 = 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.03, 0.04, 0.07, 0.11, 0.19, 0.27, 0.42, 0.60, 0.90,1.33, 1.92, 2.78, 4.17, 6.30, 9.07, 12.83, 13.65, 13.65, 13.65
y2 = 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.03, 0.04, 0.07, 0.11, 0.19, 0.27, 0.42, 0.60, 0.90,1.33, 1.92, 2.78, 4.17, 6.30, 9.07, 12.83, 13.65, 13.65, 13.65
y3=0.637,0.627,0.621,0.613,0.603,0.594,0.584,0.575,0.565,0.555'''

def picture1(y1,name):
    x1, x2 = x_rays()
    plt.figure()
    plt.title('在{}温度下，U2-U1图像'.format(name))
    plt.xlabel('u1')
    plt.ylabel('u2')
    plt.scatter(x1, y1, label='真实值')
    A, B = op.curve_fit(curve_fit1, x1, y1)[0]
    x = np.arange(0.23, 0.5, 0.01)
    y = A * 2.71314 ** (B * x)
    plt.plot(x, y, color='red', label='拟合曲线')
    plt.legend()
    plt.savefig('./img/{}.png'.format(name))
    return B
def picture2(z):
    name = '温度'
    x1, x2 = x_rays()
    plt.figure()
    plt.title('Ube-T图像')
    plt.xlabel('T')
    plt.ylabel('Ube')
    plt.scatter(x2, z, label='真实值')
    A,B = op.curve_fit(curve_fit2, x2, z)[0]
    x = np.arange(300, 350)
    y = A * x +B
    plt.plot(x, y, color='red', label='拟合曲线')
    plt.legend()
    plt.savefig('./img/{}.png'.format(name))
    return B,A
def main1():
    sele()
    se=int(input('请选择'))
    while se!=0:
        if se == 1:
            y1 = input('请用输入27度数据u,并以逗号隔开').split(',')
            y2 = input('请用输入35度数据u,并以逗号隔开').split(',')
            x = [x / 100 for x in range(23, 51, 1)]
            print(len(y1),len(y2),len(x))
            print(picture1(conver(y1), name=27))
            print(picture1(conver(y2), name=35))
        elif se==2:
            y3 = input('请输入数据u，并以逗号隔开').split(',')
            print(picture2(conver(y3)))
        sele()
        se = int(input('请选择'))
main1()






