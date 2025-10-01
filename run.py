from functions import *
import matplotlib.pyplot as plt

t1, y1 = generate_sine(1, 1)
t2, y2 = sine_time_shifting(1, 1, shift=1.4)

plt.plot(t1, y1, label="original graph")
plt.plot(t2, y2, label="time shifted by 2")
plt.title("Sinusoidal Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()