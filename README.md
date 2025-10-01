This project generates and manipulates basic signals, such as sine waves and unit step signals, using Python


functions.py
- generates sine and unit step functions
- performs time shifting and time scafling 
- each function rquires input variables such as:
    - f = frequency
    - A = amplitude
    - T = time range which will be shown on the graph
    - t0 = initial time

run.py
- runs the functions and plots them on graphs



Example ---------- 

from functions import generate_sine
import matplotlib.pyplot as plt

t, y = generate_sine(1, 1)
plt.plot(t, y)
plt.show()