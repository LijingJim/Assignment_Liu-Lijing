'''
Created on 7 Dec. 2022.
@author     : Lijing Liu (lliubo@connect.ust.hk)
Description : Bisection method
'''

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1) class 2) function 3) global variables and 4) function run

class Fig:
    sub = None
    xlabel = None
    ylabel = None
    title = None
    plota = None
    plotb = None
    # lima = None
    # limb = None  
    
    def __init__(self, sub, xlabel, ylabel, title, plota, plotb):    
        self.sub = sub
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.plota = plota
        self.plotb = plotb
        # self.lima = lima
        # self.limb = limb

    def plt_subfigure1(self):
        plt.subplot(2,3,self.sub)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.plot(self.plota,self.plotb)
        return plt  

    def plt_subfigure2(self,lima,limb):
        Fig.plt_subfigure1(self)
        plt.xlim(lima,limb)
        return plt
    
    def plt_subfigure3(self,lima,limb,posx,posy):
        Fig.plt_subfigure2(self,lima,limb)
        plt.scatter(posx,posy,c='black')
        

# objective function
def fun(x):
    return x**3-x**2-1

# for loop solution
def Bisect_For(lowInt, uppInt, maxErr):
    testArr = [] 
    testArr.append((lowInt, uppInt))
    
    for a, b in testArr: 
        try: # for boundary checking
            if a>b or fun(a)*fun(b)>0 or fun(a) == fun(b) or abs(a-b) < maxErr:
                raise ValueError
        
            if abs(fun(a)*fun(b)) < maxErr :
                if abs(fun(a)) < maxErr:
                    return a
                if abs(fun(b)) < maxErr:
                    return b
                else:
                    pass
        except ValueError:
            print("Interval setting is wrong")
        
        c = (a+b)/2
        if abs(fun(c)) < maxErr:
            return c
        if fun(c)*fun(b) < 0:
            testArr.append((c,b)) 
        else:
            testArr.append((a,c))

# while loop solution 
def Bisect_While(fun, lowInt, uppInt):
    # counting
    number = 0
    a      = lowInt
    b      = uppInt
    
    try:
        #try mistake
        if a>b or fun(a)*fun(b)>0 or fun(a) == fun(b) or abs(a-b) < 0.05:
            raise ValueError
        #try answer
        if fun(a)*fun(b) == 0:
            if func(a) == 0:
                return a
            else:
                return b
        # else we try to use False Position
        while True:
            number+=1
            abs_list.append(abs(a-b))
            # function creating
            c=(a+b)/2
            list_x.append(c)
            # judgement
            if fun(c)==0:
                return c
            if fun(c)*fun(b)<0:
                a=c
            else:
                b=c
            if abs(fun(a))<10e-6:
                return a
            if number >= 100:
                print("too much numbers")
                return None           
    except ValueError:
        print("wrong problem")
        return None

# Global Variables 
xLow    = 1
xUp     = 2 
x = np.arange(xLow,xUp,0.05)
y = fun(x)
list_x=[] 
abs_list=[]


# Try for loop solution
epsilon = 10e-6
print(Bisect_For(xLow, xUp, epsilon))

# Try while loop solution
x0 = Bisect_While(fun, xLow, xUp)
if x0 != None:   
    print("answer = ",x0)
    print("f(x0) = ",fun(x0))

# Scipy solution
root = optimize.bisect(fun, 1, 2)
print("answer =", root)

# plot and animation
plt.style.use('ggplot') 
fig = plt.figure(figsize = (15, 10))
x1 = Fig(1,'X','Y','f(x)=x^3-x^2-1 figure', x , y )
x2 = Fig(2,'X','Y','f(x)=x^3-x^2-1 figure', x , y )
x3 = Fig(3,'times of try','xo','Convergence of x0',range(len(list_x)), list_x)
x4 = Fig(4,'times of try','f(x)','Convergence of f(x)',range(len(list_x)), [fun(x) for x in list_x])
x5 = Fig(5,'times of try','|a-b|','Convergence of |a-b|',range(len(list_x)), abs_list)
x1.plt_subfigure2(1,2)
x2.plt_subfigure3(1,2,x0,fun(x0))
x3.plt_subfigure1()
x4.plt_subfigure1()
x5.plt_subfigure1()

# making animation of convergence of x0
x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0,18)
ax.set_ylim(1,2)
line, = ax.plot(0,0)

def animation_demo(i):  
    if i<17:
        x_data.append(i+1)
        y_data.append(list_x[i])
        line.set_xdata(x_data)
        line.set_ydata(y_data)
    return line

animation = FuncAnimation(fig, func = animation_demo, frames= 20, interval = 1000)
# animation
plt.show()
# animation.save("C:\\Users\\A\\Desktop\\Dajung assignment\\convergence.gif",fps=20, writer='pillow')