'''
Created on 24 Dec. 2022.
@author     : Lijing Liu (lliubo@connect.ust.hk)
Description : Newton's method
'''

import numpy as np
import matplotlib.pyplot as plt
from figureClass import Fig
from matplotlib import rc
import time
rc('font',**{'family':'serif'})
rc('text', usetex=True)
# 1) class 2) function 3) global variables and 4) function run
        
# ===========================================
# Function: function for test
# input   : x
# output  : x^3-x^2-1  
#=============================================
def fun(x):
    return x**3-x**2-1

# ===========================================
# Function: derivation of function for test
# input   : x
# output  : 3x^2-2x-1  
#=============================================
def fun1(x):
    return 3*x**2-2*x

# ===========================================
# Function: Newton's method with for loop
# inputs  : func1     = function which will be computed
#           func2     = derivation of func1
#           maxErr    = maximum error for convergence
# outputs : x0|func(x0) = 0
#=============================================
def Newton_For(func1,func2,x0,maxErr = 10e-6):
    testArr = [] 
    testArr.append(x0)
    
    for x0 in testArr: 
        try: # for boundary checking
            if abs(func1(x0)) < maxErr:
                raise ValueError
        except ValueError:
            print("Initial setting is wrong")
        
        x=x0-func1(x0)/func2(x0)
        if abs(func1(x)) < maxErr:
            return x
        else:
            testArr.append(x)

# ===========================================
# Function: Newton's method with while loop
# inputs  : func1     = function which will be computed
#           func2     = derivation of func1
#           maxErr    = maximum error for convergence
# outputs : x0|func(x0) = 0
#=============================================
def Newton_While(func1, func2, x0, maxErr = 10e-6):
    # counting
    number   = 0
    list_x   = [x0] 
    list_y   = []
    
    try:
        #try mistake
        if abs(func1(x0)) < maxErr:
            raise ValueError
        #try answer
        if func1(x0) == 0:
            return x0, list_x, list_y 
        # else we try to use Newton's Position
        while True:
            number+=1
            list_y.append(func1(x0))
            # funcction creating
            c=x0-func1(x0)/func2(x0)
            list_x.append(c)
            # judgement
            if func1(c)==0:
                return c, list_x, list_y 
            else:
                x0=c
            if abs(func1(c)) < maxErr:
                return x0, list_x, list_y  # final solution
            if number >= 100:
                print("too much numbers")
                return None           
    except ValueError:
        print("wrong problem")
        return None


# ===========================================
# Function: 4 figures (row:2, column:3)
# inputs  : x0       = x0 |func(x0)=0
#           y0       = fun(x0)
#           list_x   = list of evolution in x0 |func(x0)=0 values
#           list_y   = list of evolution in func(x0) values
#           x        = list of x values  
#           y        = list of y values
# outputs : Figure(0,0) = x vs y
#           Figure(0,1) = x vs y with x0 and y0
#           Figure(0,2) = number of iterations vs list_x
#           Figure(1,0) = number of iterations vs list_y
#=============================================
def plotIteratoins(x0, y0, list_x, list_y, x, y):
    plt.style.use('ggplot') 
    fig = plt.figure(figsize = (15, 10))
    x1 = Fig(1,'X','Y',r'$f(x)=x^3-x^2-1$', x , y )
    x2 = Fig(2,'X','Y',r'$f(x)=x^3-x^2-1$', x , y )
    x3 = Fig(3,'Iterations',r'$x_{0}$',r'Convergence of $x_{0}$',range(len(list_x)), list_x)
    x4 = Fig(4,'Iterations',r'$f(x)$',r'Convergence of $f(x)$',range(len(list_x)), list_y)
    x5 = Fig(5,'Iterations',r'log $y$',r'Convergence of log $y$',range(len(list_x)), np.log(list_y))
    
    x1.plt_subfigure2(1,2)
    x2.plt_subfigure3(1, 2, x0, y0)
    x3.plt_subfigure1()
    x4.plt_subfigure1()
    x5.plt_subfigure1()

    plt.show()
    return

# Timer Function
def TimeCal(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print('time cost: %.8f'%(end-start))
    return wrapper

# ===========================================
# Function: code test
# inputs  : testIndex
# outputs : testIndex = 0 : for testing Newton's method with scipy optimization 
#           testIndex = 1 : for testing Newton's method with for loop
#           testIndex = 2 : for testing Newton's method with while loop 
#           testIndex = 3 : for testing visualization
#           testIndex = 4 : for testing animation
#=============================================
@TimeCal
def testPosition(testIndex):
# Global Variables 
    xLow     = 1
    xUp      = 2 
    stepSize = 0.05
    # Try for loop solution
    if testIndex == 0:
        from scipy import optimize
        root = optimize.newton(fun, 1, fprime=lambda x: 3*x**2-2*x) # Scipy solution 
        print("answer =", root)
    elif testIndex == 1:
        root = Newton_For(fun,fun1,1)
        print("answer =", root)
    elif testIndex == 2:
        root, list_x, list_y = Newton_While(fun, fun1, 1)
        print("answer =", root)
    elif testIndex == 3:
        root, list_x, list_y = Newton_While(fun, fun1, 1)
        xRoot  = root 
        yRoot  = fun(root)
        x      = np.arange(xLow,xUp,stepSize)
        y      = fun(x)
        list_x = np.array(list_x)
        list_y = fun(list_x)
        plotIteratoins(xRoot, yRoot, list_x, list_y, x, y)
    elif testIndex == 4:
        from matplotlib.animation import FuncAnimation
        root, list_x, list_y = Newton_While(fun, fun1, 1)
        fig, ax                 = plt.subplots()
        ax.set_xlim(0,6)
        ax.set_ylim(1,2)
        ax.set_xlabel('Iterations')
        ax.set_ylabel('x')
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
        animation.save("convergence_Newton.gif")
        plt.show()
    return 


############
# testBisection(textIndex)
# testIndex = 0 : for testing output of bisection method with scipy optimization as comparasion with false position method
# testIndex = 1 : for testing false position method with for loop
# testIndex = 2 : for testing false position method with while loop 
# testIndex = 3 : for testing visualization
# testIndex = 4 : for testing animation
############

testPosition(3)