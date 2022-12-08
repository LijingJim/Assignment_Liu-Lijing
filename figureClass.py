import matplotlib.pyplot as plt

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