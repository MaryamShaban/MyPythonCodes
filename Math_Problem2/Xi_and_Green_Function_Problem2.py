import numpy as np
import matplotlib.pyplot as plt

# Define Green's function
def green_function(x, xi):
    return np.where(x < xi, (1 - xi) * x, (1 - x) * xi)

# Define different values of ξ
xi_values = [0.2, 0.5, 0.8]  # Sample ξ values
x = np.linspace(0, 1, 500)   # Define x range

# Plot
plt.figure(figsize=(8, 6))
for xi in xi_values:
    G = green_function(x, xi)
    plt.plot(x, G, label=f"$\\xi = {xi}$")

plt.title("Green's Function for Different $\\xi$")
plt.xlabel("$x$")
plt.ylabel("$G(x, \\xi)$")
plt.grid(True)
plt.legend()
plt.show()
