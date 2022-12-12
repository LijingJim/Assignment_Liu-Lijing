from bisectionMethod import Bisect_For


# objective function
def fun(x):
    return x**2-2*x+1

print(Bisect_For(fun, 0, 2, 10e-3))