import numpy as np
import matplotlib.pyplot as plt

# Define parameters for the problem
a = 200  # Domain range for Re(lambda)
R = 120  # Radius of the circular contour CR

# Define the poles
poles = [40, 80, 120, 160, 200]  # Real axis poles for lambda_n

# Define eigenfunctions for spectral representation
def phi_n(x, n):
    return np.sqrt(2 / a) * np.sin(n * np.pi * x / a)

# Spectral representation of delta(x - x0)
def delta_spectral(x, x0, poles):
    return sum(phi_n(x, n + 1) * phi_n(x0, n + 1) for n, _ in enumerate(poles))

# Create the circular contour CR
theta = np.linspace(0, 2 * np.pi, 500)
x_circle = R * np.cos(theta)
y_circle = R * np.sin(theta)

# Points to evaluate delta(x - x0)
x_vals = np.linspace(0, a, 500)
x0 = 100  # Location for delta function
delta_vals = delta_spectral(x_vals, x0, poles)

# Plotting the figure
plt.figure(figsize=(10, 6))
plt.plot(x_circle, y_circle, 'b-', label='$C_R$: Contour at radius R', linewidth=1.5)
plt.plot([0, a], [0, 0], 'g--', label='Branch Cut', linewidth=1.2)

for pole in poles:
    plt.plot(pole, 0, 'rx', markersize=10, label='Pole $\lambda_n$' if pole == poles[0] else "")
    plt.text(pole, -10, f'$\lambda = {pole}$', color='red', fontsize=10, ha='center')

plt.plot(x_vals, delta_vals * 20, 'm-', label='Spectral Approx. of $\delta(x - x_0)$ (scaled)', linewidth=1.5)
plt.scatter([x0], [0], color='purple', label='$x_0$: Center of $\delta$', zorder=5)

plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.xlabel('Re($\lambda$)', fontsize=12)
plt.ylabel('Im($\lambda$)', fontsize=12)
plt.title('Polar Representation in Complex $\lambda$-Plane with Spectral $\delta$', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.xlim(-R - 20, a + 20)
plt.ylim(-R - 20, R + 20)

plt.show()
