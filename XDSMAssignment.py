'''
Created on 4 Jan. 2023.
@author     : Lijing Liu (lliubo@connect.ust.hk)
Description : XDSM Assignment
'''

from pyxdsm.XDSM import (
    XDSM,
    SOLVER,
    IFUNC,
    FUNC,
    METAMODEL,
    LEFT,
)

x = XDSM()

# Create System
x.add_system("MI", SOLVER, (r"\text{Misson}", r"\text{Integration}"))
x.add_system("MM", FUNC, (r"\text{Mass}", r"\text{Model}"))
x.add_system("GM", FUNC, (r"\text{Gravitational}", r"\text{Model}"))
x.add_system("CMCC", IFUNC, (r"\text{Constant Mach/CAS}", r"\text{Conditions}"))
x.add_system("FD", SOLVER, (r"\text{Flight}", r"\text{Dynamics}"))
x.add_system("IN", FUNC, "Integrator")
x.add_system("AV", FUNC, (r"\text{Angular}", r"\text{Velocity}"))
x.add_system("BEF", FUNC, (r"\text{Body} \to \text{Earth}", r"\text{Frame}"))
x.add_system("INT", FUNC, "Integrator")
x.add_system("EOM", FUNC, (r"\text{Equation}", r"\text{of Motion}"))
x.add_system("AM", FUNC, (r"\text{Atmospheric}", r"\text{Model}"))
x.add_system("AEM", METAMODEL, (r"\text{Aerodynamic}", r"\text{Model}")) 
x.add_system("PM", METAMODEL, (r"\text{Propulsion}", r"\text{Model}"))

# Create Connection
x.connect("MI", "MM", "m", label_width=2)
x.connect("MM", "MI", ["\Vec{W} , \Delta m_{fuel}"])
x.connect("GM", "MM", "\Vec{g}")
x.connect("GM", "MI", "\Vec{g}")
x.connect("FD", "GM", "h")
x.connect("FD", "CMCC", "h")
x.connect("FD", "IN", "\Delta t")
x.connect("IN", "FD", "\Vec{r}^E")
x.connect("MM", "EOM", "\Vec{W}")
x.connect("PM", "MM", ["F_T,SFC"])
x.connect("CMCC", "AV", r'\alpha')
x.connect("CMCC", "AEM", r'\alpha')
x.connect("CMCC", "PM", r'\tau')
x.connect("AM", "CMCC", ["M,V_{CAS}"])
x.connect("MI", "FD", "\Delta t")
x.connect("BEF", "FD", "\Vec{V}^E")
x.connect("EOM", "FD", "\Vec{a}")
x.connect("EOM", "INT", "\Vec{a}")
x.connect("FD", "INT", "\Delta t")
x.connect("FD", "EOM", "\Vec{V}^E")
x.connect("FD", "AM", ["h,V^E"])
x.connect("BEF", "IN", "\Vec{V}^E")
x.connect("AV", "BEF", "\Vec{\omega}")
x.connect("AV", "EOM", "\Vec{\omega}")
x.connect("INT", "BEF", "\Vec{V}")
x.connect("AEM", "EOM", "\Vec{F_A}")
x.connect("PM", "EOM", "\Vec{F_T}")
x.connect("AM", "AEM", [r'\rho',"V_{TAS}"],label_width=2)
x.connect("AM", "PM", [r'\rho',"p_{amb},T_{amb},M"],label_width=2)

# Setting input and output for system
x.add_input("MI", ["m_0 , \Delta t"])
x.add_output("MI", ["m_{fuel} , m_{ZFW}"], side=LEFT)
x.add_input("CMCC", ["h^* , M^*, CAS^*"])
x.add_input("FD", ["\Vec{r_0} , \Vec{V_0}, \Vec{a_0}"])
x.add_input("AEM", ["S_{wing}" , r'\alpha', r'\eta'], label_width=3)
x.add_input("PM", ["BPR , n_{eng}, F_{T_{ref}}"])

# Adding process for system
x.add_process([ "MI", "CMCC", "FD", "AM", "AEM", "PM"], arrow=True)
x.add_process([ "PM","EOM", "INT", "BEF", "IN", "CMCC", "GM", "MM", "MI"], arrow=True)

# create pdf
x.write("try_assign", cleanup=False)
x.write_sys_specs("try_assign")