# DESCRIPTION:
# This algorithm finds a solution (x) for the equation f(x) = y using the bisection method.

# PARAMETERS: 
# y - Enter any real number you want
y = 15 # For example 15
# f(x) - Enter your function expression (must be a continuous function between a and b)
f = lambda x : x**2 # For example, f(x) = x^2 so we want to solve x^2 = 15 (the square root of 15)

#-------- BISECTION METHOD --------

g = lambda x : f(x) - y # We're going to solve g(x) = 0 (f(x) = y)
# Initialization of the searching interval [a,b] (a < b)
a = 1
b = 8
mid = (a+b)/2 # Midpoint of the interval

# Tolerance for the solution
eps = 0.001

# Max number of iteration in case it does not converge
MAX_ITERATIONS = 50
nb_iterations = 0

while not abs(b-a) < eps and nb_iterations < MAX_ITERATIONS:
    if g(a)*g(mid) < 0:
        b = mid 
    elif g(mid)*g(b) < 0: 
        a = mid
    else:
        print(f"There is no solution in the interval [a={a},b={b}].")
        break
    mid = (a+b)/2
    nb_iterations += 1

if nb_iterations == MAX_ITERATIONS:
    print("THE ALGORITHM DOES NOT CONVERGE TO A SOLUTION")
else:
    print(f"\nTHE ALGORITHM CONVERGES TO A SOLUTION ({nb_iterations} iterations) \nand the solution is: x = {mid} (tolerance = {eps})\n")


    










