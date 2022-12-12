'''
Created on 7 Dec. 2022.
@author     : Lijing Liu (lliubo@connect.ust.hk)
Description : Bisection method
'''

import numpy as np
import matplotlib.pyplot as plt
from figureClass import Fig

# 1) class 2) function 3) global variables and 4) function run
        
# ===========================================
# Function: function for test
# input   : x
# output  : x^3-x^2-1  
#=============================================
def fun(x):
    return x**3-x**2-1

# ===========================================
# Function: bisection method with for loop
# inputs  : func      = function which will be computed
#           lowInt    = upper bound of given interval for x
#           uppInt    = upper bound of given interval for x
#           maxErr    = maximum error for convergence
# outputs : x0|func(x0) = 0
#=============================================
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

# ===========================================
# Function: bisection method with while loop
# inputs  : func      = function which will be computed
#           lowInt    = upper bound of given interval for x
#           uppInt    = upper bound of given interval for x
#           maxErr    = maximum error for convergence
# outputs : x0|func(x0) = 0
#           list_x    = evolution of x0
#           abs_list  = | uppInt' - lowInt' |
#=============================================
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


# ===========================================
# Function: 5 figures (row:2, column:3)
# inputs  : x0       = x0 |func(x0)=0
#           y0       = fun(x0)
#           list_x   = list of evolution in x0 |func(x0)=0 values
#           list_y   = list of evolution in func(x0) values
#           x        = list of x values  
#           y        = list of y values
#           abs_list = | uppInt' - lowInt' |
# outputs : Figure(0,0) = x vs y
#           Figure(0,1) = x vs y with x0 and y0
#           Figure(0,2) = number of iterations vs list_x
#           Figure(1,0) = number of iterations vs list_y
#           Figure(1,1) = number of iterations vs abs_list
#=============================================
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
        x_data    = []    
        y_data    = []
        
        def animation_demo(i):     
            if i<len(list_x)-1:
                x_data.append(i+1)
                y_data.append(list_x[i])
                ax.plot(x_data, y_data, color='r')
            return 

        animation               = FuncAnimation(fig, 
                                                func     = animation_demo, 
                                                frames   = len(list_x), 
                                                interval = 100,
                                                repeat   = False
                                                )
        # animation.save("convergence.gif")
        plt.show()
    return

############
# testBisection(textIndex)
# testIndex = 0 : for testing bisection method with scipy optimization 
# testIndex = 1 : for testing bisection method with for loop
# testIndex = 2 : for testing bisection method with while loop 
# testIndex = 3 : for testing visualization
# testIndex = 4 : for testing animation
############

testBisection(4)


