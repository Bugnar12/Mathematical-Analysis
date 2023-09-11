import numpy as np
import matplotlib.pyplot as plt

# Define the matrix A for minimum
A1 = [[1, 0], [0, 1]]

# Define the quadratic function f
def f1(x, y, A1):
    return x*A1[0][0]*x + x*A1[0][1]*y + y*A1[1][0]*x + y*A1[1][1]*y

#IMPORTANT SPECIFICATION : I have not used the builtin function of the dot product since for some
#weird reason it did not work properly, so I chose the classical way of doing it

# Generate a grid of x and y values
x, y = np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Compute the function values at each point on the grid
Z1= f1(X, Y, A1)

# Plot the contour graph with 3 contour lines
plt.contour(X, Y, Z1, levels=[0, 1, 2])
plt.xlabel('x')
plt.ylabel('y')

# Compute the gradient of the function at 3 different points
dx, dy = np.gradient(f1(X, Y, A1))
# Plot the gradient field
plt.quiver(X[::20], Y[::20], dx[::20], dy[::20], color='r')
plt.show()

# Define the matrix A for maximum
A2 = [[-1, 0], [0, -1]]

# Define the quadratic function f
def f2(x, y, A2):
    return x*A2[0][0]*x + x*A2[0][1]*y + y*A2[1][0]*x + y*A2[1][1]*y

# Generate a grid of x and y values
x, y = np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Compute the function values at each point on the grid
Z2 = f2(X, Y, A2)

# Plot the contour graph with 3 contour lines
plt.contour(X, Y, Z2, levels=[0, 1, 2])
plt.xlabel('x')
plt.ylabel('y')

# Compute the gradient of the function at 3 different points
dx, dy = np.gradient(f2(X, Y, A2))
# Plot the gradient field
plt.quiver(X[::20], Y[::20], dx[::20], dy[::20], color='r')
plt.show()


# Define the matrix A for saddle point
A3 = [[1, -1], [-1, 1]]

# Define the quadratic function f
def f3(x, y, A3):
    return x*A3[0][0]*x + x*A3[0][1]*y + y*A3[1][0]*x + y*A3[1][1]*y

# Generate a grid of x and y values
x, y = np.linspace(-5, 5, 100), np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Compute the function values at each point on the grid
Z = f3(X, Y, A3)

# Plot the contour graph with 3 contour lines
plt.contour(X, Y, Z, levels=[0, 1, 2])
plt.xlabel('x')
plt.ylabel('y')

# Compute the gradient of the function at 3 different points
dx, dy = np.gradient(f3(X, Y, A3))
# Plot the gradient field
plt.quiver(X[::20], Y[::20], dx[::20], dy[::20], color='r')
plt.show()
