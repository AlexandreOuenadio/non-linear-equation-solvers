
#-------- BISECTION METHOD --------

# DESCRIPTION:
# The algorithm aims to find a solution (x) for the equation f(x) = y using the bisection method.

# PARAMETERS: 
# y - Enter any real number you want
y = 15
# f(x) - must be a continuous function between a and b
f = lambda x : x**2 # For example, f(x) = x^2 so we want to solve x^2 = y (the square root of y)

# ALGORITHM:
g = lambda x : f(x) - y #We're going to check if g(x) = 0 (f(x) = y)
#initialization of the searching interval [a,b] (a < b)
a = 1
b = 8
mid = (a+b)/2 #midpoint of the interval

# tolerance for the solution
eps = 0.001

while not abs(b-a) < eps:
    if g(a)*g(mid) < 0:
        b = mid 
    elif g(mid)*g(b) < 0: 
        a = mid
    else:
        print(f"There is no solution in the interval [a={a},b={b}].")
        break
    mid = (a+b)/2

print(f"The solution of the equation f(x) = {y} is approximatively equal to x = {mid}")
    










