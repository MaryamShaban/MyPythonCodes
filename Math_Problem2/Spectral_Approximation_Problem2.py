import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 200    # Domain length for x ∈ [0, a]
R = 120    # Radius of circular contour
xi = 100   # Position of delta function (renamed from x0 to xi)
N = 11     # Number of eigenfunctions to use

# Eigenfunctions and delta approximation
x_vals = np.linspace(0, a, 1000)
delta_approx = np.zeros_like(x_vals)

for n in range(N):
    u_n = np.sqrt(2/a) * np.sin((n+1)*np.pi*x_vals/a)  # Normalized eigenfunction
    u_n_xi = np.sqrt(2/a) * np.sin((n+1)*np.pi*xi/a)   # u_n(xi)
    delta_approx += u_n * u_n_xi                       # Spectral sum

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_vals, delta_approx, 'm-', label='Spectral Approx. of $\delta(x - \\xi)$')
plt.axvline(xi, color='r', linestyle='--', label='$\\xi = 100$')

# Formatting
plt.xlabel('$x$', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.title('Spectral Approximation of $\delta(x - \\xi)$', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()