'''
Created on 7 Dec. 2022.
@author     : Lijing Liu (lliubo@connect.ust.hk)
Description : Bisection method
'''

import numpy as np
import matplotlib.pyplot as plt

from figureClass import Fig

# 1) class 2) function 3) global variables and 4) function run
        

# objective function
def fun(x):
    return x**3-x**2-1

# for loop solution
def Bisect_For(func, lowInt, uppInt, maxErr = 10e-6):
    testArr = [] 
    testArr.append((lowInt, uppInt))
    
    for a, b in testArr: 
        try: # for boundary checking
            if a>b or func(a)*func(b)>0 or func(a) == func(b) or abs(a-b) < maxErr:
                raise ValueError
        
            if abs(func(a)*func(b)) < maxErr :
                if abs(func(a)) < maxErr:
                    return a
                if abs(func(b)) < maxErr:
                    return b
                else:
                    pass
        except ValueError:
            print("Interval setting is wrong")
        
        c = (a+b)/2
        if abs(func(c)) < maxErr:
            return c
        if func(c)*func(b) < 0:
            testArr.append((c,b)) 
        else:
            testArr.append((a,c))

# while loop solution 
def Bisect_While(func, lowInt, uppInt, maxErr = 10e-6):
    # counting
    number   = 0
    a        = lowInt
    b        = uppInt
    list_x   = [] 
    abs_list = []
    
    try:
        #try mistake
        if a>b or func(a)*func(b)>0 or func(a) == func(b) or abs(a-b) < maxErr:
            raise ValueError
        #try answer
        if func(a)*func(b) == 0:
            if func(a) == 0:
                return a, list_x, abs_list 
            else:
                return b, list_x, abs_list 
        # else we try to use False Position
        while True:
            number+=1
            abs_list.append(abs(a-b))
            # funcction creating
            c=(a+b)/2
            list_x.append(c)
            # judgement
            if func(c)==0:
                return c, list_x, abs_list 
            if func(c)*func(b)<0:
                a=c
            else:
                b=c
            if abs(func(a)) < maxErr:
                return a, list_x, abs_list  # final solution
            if number >= 100:
                print("too much numbers")
                return None           
    except ValueError:
        print("wrong problem")
        return None


def plotIteratoins(x0, y0, list_x, list_y, x, y, abs_list):
    plt.style.use('ggplot') 
    fig = plt.figure(figsize = (15, 10))
    x1 = Fig(1,'X','Y','f(x)=x^3-x^2-1 figure', x , y )
    x2 = Fig(2,'X','Y','f(x)=x^3-x^2-1 figure', x , y )
    x3 = Fig(3,'Iterations','xo','Convergence of x0',range(len(list_x)), list_x)
    x4 = Fig(4,'Iterations','f(x)','Convergence of f(x)',range(len(list_x)), list_y)
    x5 = Fig(5,'Iterations','|a-b|','Convergence of |a-b|',range(len(list_x)), abs_list)
    x1.plt_subfigure2(1,2)
    x2.plt_subfigure3(1, 2, x0, y0)
    x3.plt_subfigure1()
    x4.plt_subfigure1()
    x5.plt_subfigure1()

    plt.show()
    return


def animation_demo(i, list_x):  
    x_data    = []    
    y_data    = []
    line      = []
    if i<17:
        x_data.append(i+1)
        y_data.append(list_x[i])
        line.set_xdata(x_data)
        line.set_ydata(y_data)
    return line


def testBisection(testIndex):
# Global Variables 
    xLow     = 1
    xUp      = 2 
    stepSize = 0.05
    # Try for loop solution
    if testIndex == 0:
        from scipy import optimize
        root = optimize.bisect(fun, 1, 2) # Scipy solution
        print("answer =", root)
    elif testIndex == 1:
        root = Bisect_For(fun, xLow, xUp)
        print("answer =", root)
    elif testIndex == 2:
        root, list_x, list_intv = Bisect_While(fun, xLow, xUp)
        print("answer =", root)
    elif testIndex == 3:
        root, list_x, list_intv = Bisect_While(fun, xLow, xUp)
        xRoot  = root 
        yRoot  = fun(root)
        x      = np.arange(xLow,xUp,stepSize)
        y      = fun(x)
        list_x = np.array(list_x)
        list_y = fun(list_x)
        plotIteratoins(xRoot, yRoot, list_x, list_y, x, y, list_intv)
    elif testIndex == 4:
        from matplotlib.animation import FuncAnimation
        root, list_x, list_intv = Bisect_While(fun, xLow, xUp)
        fig, ax                 = plt.subplots()
        ax.set_xlim(0,18)
        ax.set_ylim(1,2)
        animation               = FuncAnimation(fig, func = animation_demo, frames= 20, interval = 1000)
        
    return

############
# testBisection(textIndex)
# testIndex = 0 : for testing bisection method with scipy optimization 
# testIndex = 1 : for testing bisection method with for loop
# testIndex = 2 : for testing bisection method with while loop 
# testIndex = 3 : for testing visualization
# testIndex = 4 : for testing animation
############

testBisection(3)


# # animation.save("C:\\Users\\A\\Desktop\\Dajung assignment\\convergence.gif",fps=20, writer='pillow')