import numpy as np
import matplotlib.pyplot as plt

# Parameters
a = 200  # Domain length for x ∈ [0, a]
R = 120  # Radius of circular contour
poles = [40, 80, 120, 160, 200]  # مقادیر ویژه λ_n = (nπ/a)²

# Plot the λ-plane
plt.figure(figsize=(10, 6))


# Circular contour
theta = np.linspace(0, 2*np.pi, 500)
x_circle = R * np.cos(theta)
y_circle = R * np.sin(theta)
plt.plot(x_circle, y_circle, 'b-', label='Contour $C_R$', linewidth=1.5)

# Poles on the real axis
plt.plot(poles, [0]*len(poles), 'rx', markersize=10, label='Poles $\lambda_n$')

# Formatting
plt.xlabel('Re($\lambda$)', fontsize=12)
plt.ylabel('Im($\lambda$)', fontsize=12)
plt.title('Complex $\lambda$-Plane with Poles and Contour', fontsize=14)
plt.axhline(0, color='k', linestyle='--', linewidth=0.5)
plt.axvline(0, color='k', linestyle='--', linewidth=0.5)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlim(-R-20, a)
plt.ylim(-R-20, R+20)
plt.show()