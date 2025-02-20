import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 200           # Domain length for x ∈ [0, a]
R = 120           # Radius of circular contour
poles = [40, 80, 120, 160, 200]  # Poles (eigenvalues λ_n)
x0 = 100          # Position of delta function
N = 5             # Number of eigenfunctions to use

#================================================================
# Plot 1: Complex λ-Plane with Poles and Contour
#================================================================
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Circular contour
theta = np.linspace(0, 2*np.pi, 500)
x_circle = R * np.cos(theta)
y_circle = R * np.sin(theta)
ax1.plot(x_circle, y_circle, 'b-', label='Contour $C_R$', linewidth=1.5)

# Poles on the real axis
ax1.plot(poles, [0]*len(poles), 'rx', markersize=10, label='Poles $\lambda_n$')

# Formatting
ax1.set_xlabel('Re($\lambda$)', fontsize=12)
ax1.set_ylabel('Im($\lambda$)', fontsize=12)
ax1.set_title('Complex $\lambda$-Plane with Poles and Contour', fontsize=14)
ax1.axhline(0, color='k', linestyle='--', linewidth=0.5)
ax1.axvline(0, color='k', linestyle='--', linewidth=0.5)
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(-R-20, a)
ax1.set_ylim(-R-20, R+20)

#================================================================
# Plot 2: Spectral Approximation of δ(x - x0)
#================================================================
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Eigenfunctions and delta approximation
x_vals = np.linspace(0, a, 1000)
delta_approx = np.zeros_like(x_vals)

for n in range(N):
    lambda_n = poles[n]  # Eigenvalue λ_n
    u_n = np.sqrt(2/a) * np.sin((n+1)*np.pi*x_vals/a)  # Normalized eigenfunction
    u_n_x0 = np.sqrt(2/a) * np.sin((n+1)*np.pi*x0/a)   # u_n(x0)
    delta_approx += u_n * u_n_x0  # Spectral sum

# Plotting
ax2.plot(x_vals, delta_approx, 'm-', label='Spectral Approx. of $\delta(x - x_0)$')
ax2.axvline(x0, color='r', linestyle='--', label='$x_0 = 100$')

# Formatting
ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel('Amplitude', fontsize=12)
ax2.set_title('Spectral Approximation of $\delta(x - x_0)$', fontsize=14)
ax2.legend()
ax2.grid(True, linestyle='--', alpha=0.6)

plt.show()