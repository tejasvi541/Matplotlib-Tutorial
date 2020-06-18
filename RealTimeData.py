import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# count function will count 1 number at a time each time we get next value
# In the function animate below we are appending to x_vals and y_vals , x_vals will get appended by one that will just count up
# by 1 , y_val is appending random int bw 0, 5.
# Lets say we wanna ti run this function every second and plot these values that are getting appended to our list
# To do this we can use the func animation class from the matplotlib animation module.


x_vals = []
y_vals = []
index = count()

# In animate funtion we will plot our x and y values, but we will get diiferent colors after each iteration because our
# plt method is plotting new line everytime clearing out old lines.
# One way to do this is to simply clear our axes. using plt.cla

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_vals, y_vals)

# First we will pass the figure we wanna animate, then animate function and then time = 1s = 1000ms
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)
# animate(10)


plt.tight_layout()
plt.show()