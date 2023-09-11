import numpy as np
import matplotlib.pyplot as plt

def f(x, y, b):
    return 0.5*(x**2 + b*y**2)

def grad_f(x, y, b):
    return np.array([x, b*y])

def grad_descent(x0, y0, b, step_size, max_iters):
    x = x0
    y = y0
    x_vals = [x0]
    y_vals = [y0]
    for i in range(max_iters):
        grad = grad_f(x, y, b)
        x = x - step_size * grad[0]
        y = y - step_size * grad[1]
        x_vals.append(x)
        y_vals.append(y)
    return x_vals, y_vals

b_values = [1, 0.5, 0.2, 0.1]
step_size = 0.1
max_iters = 50

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y, 1)

plt.figure()
plt.contour(X, Y, Z)
for b in b_values:
    x_vals, y_vals = grad_descent(5, 5, b, step_size, max_iters)
    plt.plot(x_vals, y_vals, label=f'b={b}')
plt.legend()
plt.show()
