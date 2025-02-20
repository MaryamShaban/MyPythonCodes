import numpy as np
import matplotlib.pyplot as plt

# Define Green's Function
def green_function(x, xi):
    return np.where(x < xi, x, xi)

# Compute u(x) based on the Green's Function
def compute_u(x, L, alpha, f, xi):
    integral1 = np.array([
        np.trapz([xi * f(xi_val) for xi_val in np.linspace(0, x_i, 100)], 
                 np.linspace(0, x_i, 100)) for x_i in x
    ])
    integral2 = np.array([
        x_i * np.trapz([f(xi_val) for xi_val in np.linspace(x_i, L, 100)], 
                       np.linspace(x_i, L, 100)) for x_i in x
    ])
    return alpha + integral1 + integral2

# Define multiple f(x) functions
def f1(x):
    return np.sin(np.pi * x)  # Sinusoidal source

def f2(x):
    return x**2  # Quadratic source

def f3(x):
    return np.exp(-x)  # Exponential decay source

# Parameters
L = 1  # Length of the domain
alpha = 1  # Boundary condition u(0) = alpha
xi = 0.5  # Arbitrary xi value for Green's Function

# Define x values
x = np.linspace(0, L, 500)

# List of functions and labels
functions = [f1, f2, f3]
labels = [
    "$f(x) = \sin(\pi x)$", 
    "$f(x) = x^2$", 
    "$f(x) = e^{-x}$"
]

# Plot results
plt.figure(figsize=(10, 6))

for f, label in zip(functions, labels):
    u = compute_u(x, L, alpha, f, xi)
    plt.plot(x, u, label=label)

# Customize plot
plt.title("Effect of Different $f(x)$ on $u(x)$")
plt.xlabel("$x$")
plt.ylabel("$u(x)$")
plt.grid(True)
plt.legend()
plt.show()
