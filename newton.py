# DESCRIPTION:
# This algorithm finds a solution (x) for the equation f(x) = y using the newton method.
# It generally converges more quickly than the secant method. 

# PARAMETERS: 
# y - Enter any real number you want
y = 15 # For example 15
# f(x) - Enter your function expression (must be a continuous and differentiable function between x0 and x1)
f = lambda x : x**2 # For example, f(x) = x^2 so we want to solve x^2 = 15 (the square root of 15)
# f'(x) - Enter the derivative of f
f_d = lambda x : 2*x # For example, if we take our last example, we know that f'(x) = 2x

#-------- NEWTON METHOD --------

g = lambda x : f(x) - y # We're going to solve g(x) = 0 (f(x) = y)
g_d = lambda x : f_d(x)
# Initialization of the sequence
x0 = 3 #It has to be not too far from the real solution

# Tolerance for the solution
eps = 0.001

# Max number of iterations in case it does not converge
MAX_ITERATIONS = 50
nb_iterations = 0

# We handle the case when g'(x0) = 0
hasStationnaryPoint = False

while not abs(g(x0)) < eps and nb_iterations < MAX_ITERATIONS:
    if g_d(x0) < 1e-15:
        hasStationnaryPoint = True 
        break
    x0 = x0 - g(x0)/g_d(x0)
    nb_iterations += 1

if hasStationnaryPoint:
    print(f"x = {x0} STATIONNARY POINT we cannot perform the task anymore")
elif nb_iterations == MAX_ITERATIONS:
    print("THE ALGORITHM DOES NOT CONVERGE TO A SOLUTION")
else:
    print(f"\nTHE ALGORITHM CONVERGES TO A SOLUTION ({nb_iterations} iterations) \nand the solution is: x = {x0} (tolerance = {eps})\n")
    










