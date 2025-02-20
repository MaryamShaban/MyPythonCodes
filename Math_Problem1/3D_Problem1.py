import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# پارامترهای مسئله
L = 1  # طول بازه
x = np.linspace(0, L, 100)
xi = np.linspace(0, L, 100)

# تولید شبکه نقاط
X, Xi = np.meshgrid(x, xi)

# محاسبه G(x, xi)
G = np.where(X < Xi, X, Xi)

# رسم نمودار سه‌بعدی
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Xi, G, cmap='viridis', edgecolor='k', alpha=0.8)

# تنظیمات نمودار
ax.set_title("3D Plot of Green's Function $G(x, \\xi)$")
ax.set_xlabel('$x$')
ax.set_ylabel('$\\xi$')
ax.set_zlabel('$G(x, \\xi)$')
plt.show()
