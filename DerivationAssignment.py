'''
Created on 6 Jan. 2022.
@author     : Lijing Liu (lliubo@connect.ust.hk)
Description : Different methods of derivation
'''

import numpy as np
import matplotlib.pyplot as plt
from figureClass import Fig
from matplotlib import rc
from sympy import *
rc('font',**{'family':'serif'})
rc('text', usetex=True)

# ===========================================
# Function: function for test
# input   : x
# output  : x^3-x^2-1  
#=============================================
def fun(x):
    return x**3-x**2-1

# ===========================================
# Function: derivation of function for error calculation
# input   : x
# output  : 3x^2-2x-1  
#=============================================
def fun1(x):
    return 3*x**2-2*x

# ===========================================
# Function: Three methods of finite differentiation with for loop
# inputs  : func      = function which will be computed
#           h         = step size for loop
#           a         = chose which type of difference to use
#=============================================
def fin(func,func1,h,a):
   x = np.arange(0,1,h)
   
   if a ==1:# forward difference for finite differentiation
       x_diff = x[:-1:]
       y = func(x)  
       forward_diff = np.diff(y)/h
       return x_diff,forward_diff
   if a ==2:# reverse difference for finite differentiation  
       x_diff = x[1::]
       y = func(x)  
       reverse_diff = np.diff(y)/h
       return x_diff,reverse_diff 
   if a ==3:# center difference for finite differentiation
       list_yd = []
       list_x  = []
       list_err = []
       for i in x:
           center_diff = (func(i+h)-func(i-h))/(h*2)
           list_yd.append(center_diff)
           list_x.append(i)
           list_err.append(center_diff-func1(i))
       return list_x,list_yd,list_err
   
# ===========================================
# Function: Symbolic differentiation for derivation
# input   : func      = function which will be computed  
#=============================================
def symb(func):
    # create a "symbol" called x
    x = Symbol('x')
    #Calculating Derivative
    derivative_f = diff(func(x),x)
    return derivative_f

# ===========================================
# Function: scipy method for derivation
# inputs  : func      = function which will be computed
#           h         = step size for loop
#           a         = chose which type of difference to use
#=============================================
def scitest(func,LowInt,HighInt):
    from scipy.misc import derivative
    for x in range(LowInt, HighInt):
        print(derivative(func, x, dx=1e-6))

# ===========================================
# Function: 6 figures (row:2, column:3)
# inputs  : x0       = x0
#           y0       = fun(x0)
#           xf       = x in forward difference 
#           yf       = derivation of forward difference for finite differentiation
#           xr       = x in reverse difference 
#           yr       = derivation of reverse difference for finite differentiation
#           xc       = x in center difference
#           yc       = derivation of center difference for finite differentiation
#           err      = error of center difference for finite differentiation
#           sym_diff = derivation for symbolic differentiation
# outputs : Figure(0,0) = x vs y
#           Figure(0,1) = derivation of forward difference for finite differentiation
#           Figure(0,2) = derivation of reverse difference for finite differentiation
#           Figure(1,0) = derivation of center difference for finite differentiation
#           Figure(1,1) = error of center difference for finite differentiation
#           Figure(1,2) = derivation for symbolic differentiation
#=============================================                
def plotIteratoins(x0,y0,xf,yf,xr,yr,xc,yc,err,sym_diff):
    plt.style.use('ggplot') 
    fig = plt.figure(figsize = (15, 10))
    x1 = Fig(1,'X','Y',r'$f(x)=x^3-x^2-1$', x0 , y0 )
    x2 = Fig(2,'X',r'Forward Difference',r'Derivation of $f(x)=x^3-x^2-1$', xf , yf )
    x3 = Fig(3,'X',r'Reserve Difference',r'Derivation of $f(x)=x^3-x^2-1$', xr , yr)
    x4 = Fig(4,'X',r'Center Difference',r'Derivation of $f(x)=x^3-x^2-1$', xc , yc)
    x5 = Fig(5,'X','error',r'Error in center difference',xc, err)
    x6 = Fig(6,'X',r'Symbolic differentiation',r'Derivation of $f(x)=x^3-x^2-1$',x0, sym_diff)
    x1.plt_subfigure1()
    x2.plt_subfigure1()
    x3.plt_subfigure1()
    x4.plt_subfigure1()
    x5.plt_subfigure1()
    x6.plt_subfigure1()

    plt.show()
    return   

# ===========================================
# Function: code test
# inputs  : testIndex
# outputs : testIndex = 0 : for testing derivation with scipy optimization 
#           testIndex = 1 : for ploting derivation output with finite differentiation and symbolic differentiation
#=============================================
def testDerivate(testIndex,size):
    # Try derivation solution
    if testIndex == 0:
        scitest(fun,1,4)# Scipy solution for different methods comparasion
    elif testIndex == 1:
        # plot figure of finite differentiation
        x0      = np.arange(0,1,size)
        y0      = fun(x0)
        x1,y1  = fin(fun,fun1,size,1)
        x2,y2  = fin(fun,fun1,size,2)
        x3,y3,err  = fin(fun,fun1,size,3)
        # plot figure of symbolic differentiation
        x = Symbol('x')
        sym_derivative = lambdify(x,symb(fun))
        sym_diff = [] 
        for i in x0:
            sym_diff.append(sym_derivative(i))
        # ploting
        plotIteratoins(x0, y0, x1, y1, x2, y2,x3,y3,err,sym_diff) 

    return

testDerivate(1,0.1)



        




