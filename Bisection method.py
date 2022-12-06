import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# objective function
def func(x):
    return x**3-x**2-1
# for loop solution
def bisection(lowInt, uppInt, maxErr):
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

xLow    = 1
xUp     = 2
epsilon = 10e-6
print(bisection(xLow, xUp, epsilon))


# for loop solution and figure/animation of finding root

# using ggplot as style
plt.style.use('ggplot') 
# making function
fun = lambda x: x**3-x**2-1
x = np.arange(a,b,0.05)
y = fun(x) 
# create figure 
fig = plt.figure(figsize = (15, 10))
# x0
list_x=[] 
# |a-b|
abs_list=[]
 
# while loop solution 
def position_method(func=fun):
    # counting
    number=0
    a=1
    b=2
    try:
        #try mistake
        if a>b or func(a)*func(b)>0 or func(a) == func(b) or abs(a-b) < 0.05:
            raise ValueError
        #try answer
        if func(a)*func(b) == 0:
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
            if func(c)==0:
                return c
            if func(c)*func(b)<0:
                a=c
            else:
                b=c
            if abs(func(a))<10e-6:
                return a
            if number >= 100:
                print("too much numbers")
                return None           
    except ValueError:
        print("wrong problem")
        return None
 
# calculate x0 
x0=position_method(fun)
if x0 != None:   
    print("answer x0 = ",x0)
    print("f(x0) = ",fun(x0))
plt.subplot(2,3,2)
plt.xlim(a, b)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('rusult of root')
plt.plot(x,y)
text = "bisect method"
if x0 != None:
    plt.scatter(x0,fun(x0),c='black')
    
else:
    plt.title('cannot converge on the interval')
        
class Fig:
    sub = None
    xlabel = None
    ylabel = None
    title = None
    plota = None
    plotb = None
    lima = None
    limb = None  
    
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

x1 = Fig(1,'X','Y','f(x)=x^3-x^2-1 figure', x , y )
x3 = Fig(3,'times of try','xo','Convergence of x0',range(len(list_x)), list_x)
x4 = Fig(4,'times of try','f(x)','Convergence of f(x)',range(len(list_x)), [fun(x) for x in list_x])
x5 = Fig(5,'times of try','|a-b|','Convergence of |a-b|',range(len(list_x)), abs_list)
x1.plt_subfigure2(1,2)
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