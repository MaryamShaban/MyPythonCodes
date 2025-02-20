import numpy as np
import matplotlib.pyplot as plt

# Problem parameters
L = 1  # Interval length
alpha = 1  # Boundary condition u(0) = alpha
xi = 0.5  # Given value of xi

# Define Green's function
def green_function(x, xi, L):
    return np.where(x < xi, (L - xi) * x / L, xi * (L - x) / L)

# Define f(x)
def f(x):
    return np.sin(np.pi * x)  # Example function

# Compute u(x)
def compute_u(x, L, alpha, f):
    integral1 = np.array([
        np.trapz(xi_vals * f(xi_vals), xi_vals)
        for xi_vals in [np.linspace(0, x_i, 100) for x_i in x]
    ])
    
    integral2 = np.array([
        np.trapz((L - xi_vals) * f(xi_vals), xi_vals)
        for xi_vals in [np.linspace(x_i, L, 100) for x_i in x]
    ])
    
    return (1 - x / L) * integral1 + (x / L) * integral2 + alpha * (1 - x / L)

# Define x points for plotting
x = np.linspace(0, L, 500)

# Compute Green's function and u(x)
G = green_function(x, xi, L)
u = compute_u(x, L, alpha, f)

# Plot
plt.figure(figsize=(12, 6))

# Plot Green's function
plt.subplot(1, 2, 1)
plt.plot(x, G, label=f"Green's Function (xi={xi})", color='b')
plt.title("Green's Function $G(x, \\xi)$")
plt.xlabel("$x$")
plt.ylabel("$G(x, \\xi)$")
plt.grid(True)
plt.legend()

# Plot u(x)
plt.subplot(1, 2, 2)
plt.plot(x, u, label="$u(x)$", color='r')
plt.title("Solution $u(x)$")
plt.xlabel("$x$")
plt.ylabel("$u(x)$")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
