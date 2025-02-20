import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# پارامترهای مسئله
L = 1
x = np.linspace(0, L, 100)
alpha = 1  # شرط مرزی u(0)

# تابع f(x)
def f(x):
    return np.sin(np.pi * x)

# تابع گرین
def green_function(x, xi):
    return np.where(x < xi, x, xi)

# محاسبه u(x)
def compute_u(x, xi, f):
    integral1 = np.trapz([xi*f(xi_val) for xi_val in np.linspace(0, x, 100)], np.linspace(0, x, 100))
    integral2 = x * np.trapz([f(xi_val) for xi_val in np.linspace(x, L, 100)], np.linspace(x, L, 100))
    return alpha + integral1 + integral2

# تنظیمات اولیه انیمیشن
fig, ax = plt.subplots(figsize=(8, 5))
line1, = ax.plot([], [], label='u(x)', color='blue')
line2, = ax.plot([], [], label="Green's Function", color='orange')
ax.set_xlim(0, L)
ax.set_ylim(0, alpha + 1)
ax.set_title('Evolution of u(x) with Changing $\\xi$')
ax.set_xlabel('$x$')
ax.set_ylabel('$u(x)$')
ax.legend()

# به‌روزرسانی انیمیشن
def update(frame):
    xi = frame / 100
    G = green_function(x, xi)
    u = np.array([compute_u(x_i, xi, f) for x_i in x])
    line1.set_data(x, u)
    line2.set_data(x, G)
    return line1, line2

# ساخت انیمیشن
ani = FuncAnimation(fig, update, frames=100, interval=100, blit=True)
plt.show()
