import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x = [0]
y = [0]

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', marker=".", markersize=1)

def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 0.5)
    return ln,

count = [0]

def update(frame):
    count[0] += 1
    print(count)
    for i in range(count[0]):
        x_new = y[-1] + 1 - 1.4 * x[-1] * x[-1]
        y_new = 0.3 * x[-1]
        x.append(x_new)
        y.append(y_new)
    xdata.append(x)
    ydata.append(y)
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update,
                    init_func=init, blit=True, interval=0)
plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
